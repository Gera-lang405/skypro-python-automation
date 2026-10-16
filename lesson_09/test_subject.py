def test_add_subject(subject_table, created_ids, unique_title):
    subject_id = subject_table.get_max_id() + 1

    subject_table.create(subject_id, unique_title)
    created_ids.append(subject_id)

    subject = subject_table.get_by_id(subject_id)
    assert subject == {"subject_id": subject_id,
                       "subject_title": unique_title}


def test_update_subject(subject_table, new_subject, unique_title):
    subject_table.update_title(new_subject["subject_id"], unique_title)

    subject = subject_table.get_by_id(new_subject["subject_id"])
    assert subject["subject_title"] == unique_title
    assert subject["subject_title"] != new_subject["subject_title"]


def test_delete_subject(subject_table, new_subject):
    subject_table.delete(new_subject["subject_id"])

    assert subject_table.get_by_id(new_subject["subject_id"]) is None
