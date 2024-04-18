function FindIntersection(strArr) {
  const firstList: number[] = strArr[0].split(", ");
  const secondList: number[] = strArr[1].split(", ");

  let matchMap: { [key: string]: true } = {};
  let resultArr: number[] = [];

  firstList.forEach((str) => (matchMap[str] = true));

  secondList.forEach((num) => {
    if (matchMap[num]) {
      resultArr.push(num);
    }
  });

  return resultArr.length > 0 ? resultArr.join(",") : "false";
}
