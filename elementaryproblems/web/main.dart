import 'dart:html';
import 'dart:math';

final DivElement wrapper = querySelector('.wrapper') as DivElement;

double remap(double x, double x1, double x2, double y1, double y2) {
  return (x - x1) / (x2 - x1) * (y2 - y1) + y1;
}

int inverseCdf(double x) {
  var numSets = [
    (0.1, 0, 9),
    (3, 10, 99),
    (5, 100, 999),
    (3, 1000, 9999),
    (1, 10000, 99999)
  ];
  var totalWeight = 0.0;
  for (final (weight, _, _) in numSets) {
    totalWeight = totalWeight + weight;
  }
  for (final (weight, begin, end) in numSets) {
    var q = weight / totalWeight;
    if (x < q) {
      return remap(x, 0, q, begin as double, end as double).round();
    } else {
      x = x - q;
    }
  }
  return 1324;
}

sealed class Problem {
  int? first;
  int? second;

  int answer();
  String getInnerHtml();
}

class AdditionProblem extends Problem {
  AdditionProblem(int first, int second) {
    if (first > second) {
      this.first = first;
      this.second = second;
    } else {
      this.first = second;
      this.second = first;
    }
  }
  @override
  int answer() {
    return first! + second!;
  }

  @override
  String getInnerHtml() {
    return '<tr><td></td><td>$first</td></tr><tr><td>+</td><td>$second</td></tr>';
  }
}

class SubtractionProblem extends Problem {
  SubtractionProblem(int first, int second) {
    if (first > second) {
      this.first = first;
      this.second = second;
    } else {
      this.first = second;
      this.second = first;
    }
  }
  @override
  int answer() {
    return first! - second!;
  }

  @override
  String getInnerHtml() {
    return '<tr><td></td><td>$first</td></tr><tr><td>&#8722;</td><td>$second</td></tr>';
  }
}

List<Problem> problems = [];
List<int> provisionalSolutions = [];

Problem makeProblem() {
  double d = Random().nextDouble();
  if (d > 0.6) {
    return AdditionProblem(
        inverseCdf(Random().nextDouble()), inverseCdf(Random().nextDouble()));
  }
  return SubtractionProblem(
      inverseCdf(Random().nextDouble()), inverseCdf(Random().nextDouble()));
}

void addProblem() {
  DivElement d = DivElement();
  d.className = "element";
  Problem p = makeProblem();
  problems.add(p);
  var t = TableElement();
  t.className = "problem";
  t.innerHtml = p.getInnerHtml();
  d.children.add(t);
  InputElement i = InputElement();
  i.onChange.listen( (_){ int input = int.parse(i.value!); if(input == p.answer()){t.style.background='green';}else{t.style.background='white';} } );
  d.children.add(i);

  wrapper.children.add(d);
}

void main() {
  for (int i = 0; i < 35; i++) {
    addProblem();
  }
}
