# Range-Scalp Bot

*Updated Wed Nov 11 18:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56049 | 48876 | 7173 (94) | 2 | $-15341.56 | -4.3% |
| **+10¢** | 41876 | 33505 | 8371 (124) | 4 | $-14328.35 | -5.4% |
| **+15¢** | 35113 | 26088 | 9025 (158) | 4 | $-13053.66 | -5.9% |
| **+20¢** | 31276 | 21808 | 9468 (208) | 5 | $-11424.43 | -5.8% |
| **+10¢ (15¢ stop)** | 68283 | 68162 | 121 (73) | 4 | $-25142.00 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 18:36 | +5 | ZEC | UP | 0.62 | 0.68 | 0.27 |
| 11-11 18:35 | +10 stop | HYPE | UP | 0.67 | open |  |
| 11-11 18:35 | +20 | HYPE | UP | 0.67 | open |  |
| 11-11 18:35 | +15 | HYPE | UP | 0.67 | open |  |
| 11-11 18:35 | +10 | HYPE | UP | 0.67 | open |  |
| 11-11 18:35 | +5 | HYPE | UP | 0.67 | 0.73 | 0.30 |
| 11-11 18:35 | +10 stop | ZEC | UP | 0.63 | open |  |
| 11-11 18:35 | +10 | ZEC | UP | 0.63 | open |  |
| 11-11 18:35 | +5 | ZEC | UP | 0.63 | 0.69 | 0.28 |
| 11-11 18:34 | +10 stop | ETH | UP | 0.69 | open |  |
| 11-11 18:34 | +20 | ETH | UP | 0.69 | open |  |
| 11-11 18:34 | +15 | ETH | UP | 0.69 | open |  |
| 11-11 18:34 | +10 | ETH | UP | 0.69 | open |  |
| 11-11 18:34 | +5 | ETH | UP | 0.69 | open |  |
| 11-11 18:34 | +10 stop | BNB | UP | 0.63 | open |  |
| 11-11 18:34 | +20 | BNB | UP | 0.63 | open |  |
| 11-11 18:34 | +15 | BNB | UP | 0.63 | open |  |
| 11-11 18:34 | +10 | BNB | UP | 0.63 | open |  |
| 11-11 18:34 | +5 | BNB | UP | 0.63 | open |  |
| 11-11 18:31 | +10 stop | NEAR | UP | 0.62 | 0.78 | 1.30 |
| 11-11 18:31 | +20 | NEAR | UP | 0.62 | 0.84 | 1.93 |
| 11-11 18:31 | +15 | NEAR | UP | 0.63 | 0.78 | 1.20 |
| 11-11 18:31 | +10 | NEAR | UP | 0.64 | 0.78 | 1.10 |
| 11-11 18:31 | +5 | NEAR | UP | 0.64 | 0.71 | 0.38 |
| 11-11 18:31 | +10 stop | XRP | UP | 0.67 | 0.82 | 1.23 |
| 11-11 18:31 | +20 | XRP | UP | 0.67 | open |  |
| 11-11 18:31 | +15 | XRP | UP | 0.67 | 0.82 | 1.23 |
| 11-11 18:31 | +10 | XRP | UP | 0.67 | 0.82 | 1.23 |
| 11-11 18:31 | +5 | XRP | UP | 0.67 | 0.72 | 0.19 |
| 11-11 18:31 | +10 stop | ZEC | UP | 0.69 | 0.81 | 0.94 |
| 11-11 18:31 | +20 | ZEC | UP | 0.68 | open |  |
| 11-11 18:31 | +15 | ZEC | UP | 0.68 | open |  |
| 11-11 18:31 | +10 | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 11-11 18:31 | +5 | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 11-11 18:28 | +10 stop | DOGE | UP | 0.17 | 0.61 | 4.13 |
| 11-11 18:28 | +20 | DOGE | UP | 0.17 | 0.61 | 4.13 |
| 11-11 18:28 | +15 | DOGE | UP | 0.17 | 0.61 | 4.13 |
| 11-11 18:28 | +10 | DOGE | UP | 0.18 | 0.61 | 4.02 |
| 11-11 18:28 | +5 | DOGE | UP | 0.19 | 0.61 | 3.92 |
| 11-11 18:27 | +10 stop | NEAR | UP | 0.47 | 0.17 | -3.28 |
