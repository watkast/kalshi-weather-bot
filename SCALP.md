# Range-Scalp Bot

*Updated Wed Nov 11 10:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55647 | 48530 | 7117 (94) | 3 | $-15203.31 | -4.3% |
| **+10¢** | 41580 | 33278 | 8302 (124) | 4 | $-14137.49 | -5.4% |
| **+15¢** | 34859 | 25906 | 8953 (158) | 7 | $-12904.06 | -5.9% |
| **+20¢** | 31046 | 21653 | 9393 (208) | 7 | $-11285.25 | -5.8% |
| **+10¢ (15¢ stop)** | 67781 | 67660 | 121 (73) | 1 | $-24939.87 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 10:13 | +10 stop | ZEC | DOWN | 0.62 | open |  |
| 11-11 10:13 | +15 | ZEC | DOWN | 0.62 | open |  |
| 11-11 10:13 | +10 | ZEC | DOWN | 0.62 | open |  |
| 11-11 10:13 | +5 | ZEC | DOWN | 0.62 | open |  |
| 11-11 10:12 | +10 stop | HYPE | DOWN | 0.71 | 0.55 | -1.93 |
| 11-11 10:11 | +10 stop | HYPE | UP | 0.30 | 0.56 | 2.25 |
| 11-11 10:10 | +10 stop | ZEC | UP | 0.63 | 0.82 | 1.62 |
| 11-11 10:08 | +10 stop | NEAR | UP | 0.61 | 0.72 | 0.78 |
| 11-11 10:07 | +10 stop | ZEC | DOWN | 0.56 | 0.38 | -2.15 |
| 11-11 10:06 | +10 stop | ZEC | UP | 0.62 | 0.42 | -2.35 |
| 11-11 10:05 | +10 stop | NEAR | DOWN | 0.59 | 0.40 | -2.23 |
| 11-11 10:05 | +10 stop | ZEC | DOWN | 0.62 | 0.39 | -2.64 |
| 11-11 10:04 | +10 stop | BTC | DOWN | 0.60 | 0.83 | 2.03 |
| 11-11 10:04 | +10 stop | HYPE | DOWN | 0.57 | 0.69 | 0.87 |
| 11-11 10:03 | +10 stop | ZEC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-11 10:03 | +10 stop | NEAR | DOWN | 0.62 | 0.46 | -1.95 |
| 11-11 10:02 | +10 stop | DOGE | DOWN | 0.68 | 0.81 | 1.03 |
| 11-11 10:02 | +10 | DOGE | DOWN | 0.68 | 0.81 | 1.03 |
| 11-11 10:02 | +5 | DOGE | DOWN | 0.68 | 0.81 | 1.03 |
| 11-11 10:02 | +10 stop | BTC | UP | 0.57 | 0.42 | -1.86 |
| 11-11 10:02 | +15 | BTC | UP | 0.57 | open |  |
| 11-11 10:02 | +5 | BTC | UP | 0.57 | open |  |
| 11-11 10:02 | +10 stop | DOGE | UP | 0.47 | 0.59 | 0.85 |
| 11-11 10:02 | +20 | DOGE | UP | 0.47 | open |  |
| 11-11 10:02 | +15 | DOGE | UP | 0.47 | open |  |
| 11-11 10:02 | +10 | DOGE | UP | 0.47 | 0.59 | 0.85 |
| 11-11 10:02 | +5 | DOGE | UP | 0.47 | 0.59 | 0.85 |
| 11-11 10:02 | +5 | ETH | UP | 0.41 | 0.58 | 1.35 |
| 11-11 10:01 | +10 stop | HYPE | UP | 0.65 | 0.47 | -2.14 |
| 11-11 10:01 | +20 | HYPE | UP | 0.65 | open |  |
| 11-11 10:01 | +15 | HYPE | UP | 0.65 | open |  |
| 11-11 10:01 | +10 | HYPE | UP | 0.65 | open |  |
| 11-11 10:01 | +5 | HYPE | UP | 0.65 | open |  |
| 11-11 10:01 | +10 stop | BNB | UP | 0.55 | 0.38 | -2.05 |
| 11-11 10:01 | +20 | BNB | UP | 0.55 | open |  |
| 11-11 10:01 | +15 | BNB | UP | 0.55 | open |  |
| 11-11 10:01 | +10 | BNB | UP | 0.55 | open |  |
| 11-11 10:01 | +5 | BNB | UP | 0.55 | 0.60 | 0.15 |
| 11-11 10:01 | +10 stop | NEAR | UP | 0.68 | 0.52 | -1.94 |
| 11-11 10:01 | +20 | NEAR | UP | 0.68 | 0.96 | 2.59 |
