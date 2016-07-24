// constructs the suggestion engine
var states = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.whitespace,
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  // `states` is an array of state names defined in "The Basics"
  local: states = [["B1001", "POLICY MANAGEMENT STUDIES", true, "Spring", false, ["Friday 3rd Period"], "Japanese"], ["B1001", "POLICY MANAGEMENT STUDIES", true, "Fall", true, ["Tuesday 1st Period(tentative)\n"], "English"], ["B1002", "ENVIRONMENT AND INFORMATION STUDIES", true, "Spring", false, ["Thursday 1st Period"], "Japanese"], ["B1002", "ENVIRONMENT AND INFORMATION STUDIES", true, "Fall", true, ["Thursday 1st Period(tentative)\n"], "English"], ["B1003", "INTRODUCTION TO KEIO GIJUKU, ITS HISTORY, PEOPLE AND TRADITION", false, "Spring", false, ["Friday 3rd Period"], "Japanese"]]
});

$('#bloodhound .typeahead').typeahead({
  hint: true,
  highlight: true,
  minLength: 1
},
{
  name: 'states',
  source: states
});