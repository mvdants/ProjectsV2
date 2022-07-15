
class JobList{

  String _title = '';
  String _description = '';
  double _gratification = 0;
  String _creatorJobName = '';

  JobList(this._title, this._description, this._gratification,
      this._creatorJobName);

  String get creatorJobName => _creatorJobName;

  double get gratification => _gratification;

  String get description => _description;

  String get title => _title;

}