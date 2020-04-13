def compareVersion(version1, version2):
        versions1 = [int(v) for v in version1.split(".")]
        versions2 = [int(v) for v in version2.split(".")]
        for i in range(max(len(versions1),len(versions2))):
            v1 = versions1[i] if i < len(versions1) else 0
            v2 = versions2[i] if i < len(versions2) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0


version1, version2 = "1.1", '1.1'
result1 = compareVersion(version1,version2)

version3, version4 = "1.2.1", '1.1'
result2 = compareVersion(version3,version4)

version5, version6 = "0.1.5.4", '0.1.6.7.8'
result3 = compareVersion(version5,version6)

print(version1, "vs", version2,"=", result1,'\n',
      version3, "vs", version4,"=", result2,'\n',
      version5, "vs", version6,"=", result3)

    