import grpc
import random
import logging
import uuid
import time

from util.environment import ENV
from util.metadata_interceptor import MetadataInterceptor

from proto import pb


METADATA = [
    (
        "authorization",
        ("Bearer eyJzdWIiOiIxODE1OTcxMy01ZDRlLTRhZDUtOTRhZC1mYmI2YmIxNDc5ODQ"
         "iLCJlbWFpbCI6InRlc3RpbmUudGVzdEBoZWxwd2F2ZS5kZSIsIm5hbWUiOiJUZXN0"
         "aW5lIFRlc3QiLCJuaWNrbmFtZSI6InRlc3RpbmUudGVzdCIsIm9yZ2FuaXphdG"
         "lvbnMiOlsiM2IyNWM2ZjUtNDcwNS00MDc0LTlmYzYtYTUwYzI4ZWJhNDA2Il19")
    )
]


def setup_grpc_client() -> None:
    global channel, task_stub, patient_stub, property_stub, property_value_stub

    interceptor = MetadataInterceptor(METADATA)

    tasks_connection = f"{ENV.SERVICES_HOST}:{ENV.TASKS_PORT}"
    property_connection = f"{ENV.SERVICES_HOST}:{ENV.PROPERTY_PORT}"

    tasks_channel = grpc.intercept_channel(
        grpc.insecure_channel(tasks_connection), interceptor)
    property_channel = grpc.intercept_channel(
        grpc.insecure_channel(property_connection), interceptor)

    task_stub = pb.TaskServiceStub(tasks_channel)
    patient_stub = pb.PatientServiceStub(tasks_channel)
    property_stub = pb.PropertyServiceStub(property_channel)
    property_value_stub = pb.PropertyValueServiceStub(property_channel)


def create_patient(human_readable_id: str, notes: str) -> uuid.UUID:
    request: pb.CreatePatientRequest = pb.CreatePatientRequest(
        human_readable_identifier=human_readable_id,
        notes=notes
    )
    response: pb.CreatePatientResponse = patient_stub.CreatePatient(
        request=request)

    logging.info(f"Created patient with id {response.id}")
    return response.id


def create_property(name: str) -> uuid.UUID:
    request: pb.CreatePropertyRequest = pb.CreatePropertyRequest(
        name=name,
        subject_type=pb.SubjectType.SUBJECT_TYPE_PATIENT,
        field_type=pb.FieldType.FIELD_TYPE_TEXT,
    )
    response: pb.CreatePropertyResponse = property_stub.CreateProperty(
        request=request)
    logging.info(f"Created property with id {response.property_id}")
    return response.property_id


def attach_property_value(patient_id: uuid.UUID, property_id: uuid.UUID,
                          value: str) -> None:
    # can also be used to update property value
    request: pb.AttachPropertyValueRequest = pb.AttachPropertyValueRequest(
        subject_id=patient_id,
        property_id=property_id,
        text_value=value
    )
    property_value_stub.AttachPropertyValue(
        request=request)
    logging.info(f"Attached property value to property with id {property_id}")


def assign_bed(bed_id: uuid.UUID, patient_id: uuid.UUID) -> None:
    request: pb.AssignBedRequest = pb.AssignBedRequest(
        bed_id=str(bed_id),
        id=str(patient_id)
    )
    patient_stub.AssignBed(request=request)
    logging.info("Assigned patient to bed")


def update_patient(patient_id: uuid.UUID, notes: str) -> None:
    request: pb.UpdatePatientRequest = pb.UpdatePatientRequest(
        id=str(patient_id),
        notes=notes
    )
    patient_stub.UpdatePatient(request=request)
    logging.info(f"Updated Patients notes to {notes}")


def discharge_patient(patient_id: uuid.UUID) -> None:
    request: pb.DischargePatientRequest = pb.DischargePatientRequest(
        id=str(patient_id)
    )
    patient_stub.DischargePatient(request=request)


def create_task(description: str, name: str,
                patient_id: uuid.UUID) -> uuid.UUID:
    request: pb.CreateTaskRequest = pb.CreateTaskRequest(
        description=description,
        name=name,
        patient_id=patient_id,
        public=True,
    )
    response: pb.CreateTaskResponse = task_stub.CreateTask(request=request)

    logging.info(f"Created task with id {
                 response.id} for patient with id {patient_id}")
    return response.id


def update_task(task_id: uuid.UUID, new_status: pb.TaskStatus) -> None:
    request: pb.UpdateTaskRequest = pb.UpdateTaskRequest(
        id=task_id,
        status=new_status
    )
    task_stub.UpdateTask(request=request)
    logging.info(f"Updated task with id {task_id} to status {new_status}")


def simulate_st_elevation_process() -> bool:
    # patient arrival and triage:
    patient_id = create_patient(f"patient_{uuid.uuid4()}", "")
    assign_bed(uuid.uuid4(), patient_id)  # assign random bed

    # create first tasks and move them directly to InProgress and then to done
    task_one_id = create_task("", "Establish standard monitoring", patient_id)
    task_two_id = create_task("", "Establish twelve channel ECG", patient_id)
    task_three_id = create_task("", "Take blood samples for lab", patient_id)
    time.sleep(random.uniform(0.1, 0.5))
    update_task(task_one_id, pb.TaskStatus.TASK_STATUS_DONE)
    update_task(task_two_id, pb.TaskStatus.TASK_STATUS_DONE)
    update_task(task_three_id, pb.TaskStatus.TASK_STATUS_DONE)

    # review disgnostic results, update notes with new information
    first_diagnosis_task = create_task("", "Monitor ECG", patient_id)
    time.sleep(random.uniform(0.1, 0.5))
    update_task(first_diagnosis_task, pb.TaskStatus.TASK_STATUS_DONE)

    if random.random() < 0.2:
        update_patient(patient_id, "ST elevation no chest pain")
    else:
        # intermediate intervention required, st elevation detected
        update_patient(patient_id, "ST elevation and reoccuring chest pain")

    intermediate_intervention_task_id = create_task(
        "", "Call Cardiologist", patient_id)
    time.sleep(random.uniform(0.1, 0.5))
    update_task(intermediate_intervention_task_id,
                pb.TaskStatus.TASK_STATUS_DONE)

    intermediate_intervention_task_id_two = create_task(
        "", "Transport to Cardiology", patient_id)
    time.sleep(random.uniform(0.1, 0.5))
    update_task(intermediate_intervention_task_id_two,
                pb.TaskStatus.TASK_STATUS_DONE)

    if random.random() < 0.2:
        if simulate_complication_process(patient_id):
            return

    intermediate_intervention_task_id_three = create_task(
        "", "Initialize narcose", patient_id)
    time.sleep(random.uniform(0.1, 0.5))
    update_task(intermediate_intervention_task_id_three,
                pb.TaskStatus.TASK_STATUS_DONE)

    medication_property_id = create_property("medication")
    attach_property_value(patient_id, medication_property_id, "anesthetic")

    intermediate_intervention_task_id_four = create_task(
        "", "Cardiac catheter examination", patient_id)
    time.sleep(random.uniform(0.1, 0.5))
    update_task(intermediate_intervention_task_id_four,
                pb.TaskStatus.TASK_STATUS_DONE)

    if random.random() < 0.3:
        if simulate_complication_process(patient_id):
            return

    intermediate_intervention_task_id_five = create_task(
        "", "Administer first medication", patient_id)
    time.sleep(random.uniform(0.1, 0.5))
    update_task(intermediate_intervention_task_id_five,
                pb.TaskStatus.TASK_STATUS_DONE)

    attach_property_value(patient_id, medication_property_id,
                          "clopidogrel, prasugrel, beta blockers")

    # patient stabelized
    update_patient(patient_id, "Patient stabilized")

    first_after_task = create_task(
        "", "Administrate long term medication", patient_id)
    time.sleep(random.uniform(0.1, 0.5))
    update_task(first_after_task, pb.TaskStatus.TASK_STATUS_DONE)

    attach_property_value(
        patient_id, medication_property_id, "aec inhibitor, statins")

    second_after_task = create_task("", "Plan patient observation", patient_id)
    time.sleep(random.uniform(0.1, 0.5))
    update_task(second_after_task, pb.TaskStatus.TASK_STATUS_DONE)

    third_after_task = create_task(
        "", "Generate discharge summary", patient_id)
    time.sleep(random.uniform(0.1, 0.5))
    update_task(third_after_task, pb.TaskStatus.TASK_STATUS_DONE)

    discharge_patient(patient_id)


def simulate_st_not_elevation_process() -> None:
    patient_id = create_patient(f"patient_{uuid.uuid4()}", "")
    assign_bed(uuid.uuid4(), patient_id)  # assign random bed

    # create first tasks and move them directly to InProgress and then to done
    task_one_id = create_task("", "Establish standard monitoring", patient_id)
    task_two_id = create_task("", "Establish twelve channel ECG", patient_id)
    task_three_id = create_task("", "Take blood samples for lab", patient_id)
    time.sleep(random.uniform(0.1, 0.5))
    update_task(task_one_id, pb.TaskStatus.TASK_STATUS_DONE)
    update_task(task_two_id, pb.TaskStatus.TASK_STATUS_DONE)
    update_task(task_three_id, pb.TaskStatus.TASK_STATUS_DONE)

    # review diagnostic results, update notes with new information
    first_diagnosis_task = create_task("", "Monitor ECG", patient_id)
    time.sleep(random.uniform(0.1, 0.5))
    update_task(first_diagnosis_task, pb.TaskStatus.TASK_STATUS_DONE)

    # Diagnosis requires additional follow-up
    update_patient(patient_id, "No ST Elevation, chest pain")
    followup_task_id = create_task("", "Plan further assessment", patient_id)
    time.sleep(random.uniform(0.1, 0.5))
    update_task(followup_task_id, pb.TaskStatus.TASK_STATUS_DONE)

    followup_task_id_two = create_task(
        "", "Measure cardiac biomarkers", patient_id)
    time.sleep(random.uniform(0.1, 0.5))
    update_task(followup_task_id_two, pb.TaskStatus.TASK_STATUS_DONE)

    followup_task_id_three = create_task(
        "", "Physical exaimination", patient_id)
    time.sleep(random.uniform(0.1, 0.5))
    update_task(followup_task_id_three, pb.TaskStatus.TASK_STATUS_DONE)

    # patient stabelized
    update_patient(patient_id, "Patient has broken sternum")

    first_after_task = create_task(
        "", "Initiate transfer to trauma unit", patient_id)
    time.sleep(random.uniform(0.1, 0.5))
    update_task(first_after_task, pb.TaskStatus.TASK_STATUS_DONE)

    discharge_patient(patient_id)


def simulate_complication_process(patient_id: uuid.UUID) -> bool:
    """
    This function is only part of a process, and simulates
    the reanimation
    """
    followup_task_id_three = create_task("", "Reanimation", patient_id)
    update_task(followup_task_id_three, pb.TaskStatus.TASK_STATUS_DONE)

    if random.random() < 0.4:
        update_patient(patient_id, "Patient died")
        discharge_patient(patient_id)
        return True
    else:
        update_patient(patient_id, "Successful reanimation")
        return False


if __name__ == "__main__":
    # setup logging
    logging.basicConfig(
        format="%(asctime)s %(levelname)-8s %(message)s",
        level=ENV.LOG_LEVEL,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    try:
        setup_grpc_client()
    except grpc.RpcError:
        logging.exception("cannot create a channel and stubs")

    # generate dataset:
    for _ in range(100):
        choice = random.random()
        if choice < 0.7:
            if simulate_st_elevation_process():
                continue
        else:
            simulate_st_not_elevation_process()

        time.sleep(random.uniform(0.5, 1.5))
