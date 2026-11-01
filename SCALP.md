# Range-Scalp Bot

*Updated Sun Nov 01 04:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43206 | 37663 | 5543 (62) | 2 | $-12274.23 | -4.5% |
| **+10¢** | 32220 | 25814 | 6406 (84) | 2 | $-10999.67 | -5.4% |
| **+15¢** | 26959 | 20056 | 6903 (112) | 3 | $-10055.59 | -5.9% |
| **+20¢** | 23942 | 16710 | 7232 (146) | 3 | $-8879.92 | -5.9% |
| **+10¢ (15¢ stop)** | 52675 | 52592 | 83 (48) | 0 | $-19907.76 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 04:40 | +10 stop | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 11-01 04:40 | +20 | HYPE | UP | 0.70 | open |  |
| 11-01 04:40 | +15 | HYPE | UP | 0.70 | open |  |
| 11-01 04:40 | +10 | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 11-01 04:40 | +5 | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 11-01 04:40 | +10 stop | BTC | DOWN | 0.61 | 0.29 | -3.52 |
| 11-01 04:40 | +10 | BTC | DOWN | 0.61 | open |  |
| 11-01 04:40 | +5 | BTC | DOWN | 0.60 | open |  |
| 11-01 04:38 | +10 stop | BTC | DOWN | 0.56 | 0.71 | 1.17 |
| 11-01 04:38 | +15 | BTC | DOWN | 0.57 | open |  |
| 11-01 04:38 | +10 | BTC | DOWN | 0.57 | 0.71 | 1.07 |
| 11-01 04:38 | +5 | BTC | DOWN | 0.57 | 0.71 | 1.07 |
| 11-01 04:35 | +5 | XRP | DOWN | 0.60 | 0.72 | 0.88 |
| 11-01 04:34 | +5 | XRP | DOWN | 0.53 | 0.59 | 0.25 |
| 11-01 04:33 | +10 stop | XRP | DOWN | 0.60 | 0.72 | 0.88 |
| 11-01 04:33 | +20 | XRP | DOWN | 0.60 | 0.81 | 1.82 |
| 11-01 04:33 | +15 | XRP | DOWN | 0.60 | 0.79 | 1.61 |
| 11-01 04:33 | +10 | XRP | DOWN | 0.60 | 0.72 | 0.88 |
| 11-01 04:33 | +5 | XRP | DOWN | 0.60 | 0.69 | 0.58 |
| 11-01 04:33 | +10 stop | BNB | DOWN | 0.70 | 0.80 | 0.73 |
| 11-01 04:33 | +20 | BNB | DOWN | 0.70 | 0.97 | 2.51 |
| 11-01 04:33 | +15 | BNB | DOWN | 0.70 | 0.86 | 1.36 |
| 11-01 04:33 | +10 | BNB | DOWN | 0.70 | 0.80 | 0.73 |
| 11-01 04:33 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 11-01 04:33 | +10 stop | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-01 04:33 | +20 | BTC | DOWN | 0.59 | open |  |
| 11-01 04:33 | +15 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-01 04:33 | +10 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-01 04:33 | +5 | BTC | DOWN | 0.60 | 0.68 | 0.47 |
| 11-01 04:32 | +5 | XRP | UP | 0.33 | 0.55 | 1.86 |
| 11-01 04:32 | +10 stop | XRP | DOWN | 0.46 | 0.73 | 2.38 |
| 11-01 04:32 | +20 | XRP | DOWN | 0.46 | 0.73 | 2.38 |
| 11-01 04:32 | +15 | XRP | DOWN | 0.46 | 0.73 | 2.38 |
| 11-01 04:32 | +10 | XRP | DOWN | 0.46 | 0.73 | 2.38 |
| 11-01 04:32 | +5 | XRP | DOWN | 0.46 | 0.55 | 0.54 |
| 11-01 04:32 | +5 | DOGE | UP | 0.57 | open |  |
| 11-01 04:31 | +10 stop | ETH | DOWN | 0.67 | 0.81 | 1.13 |
| 11-01 04:31 | +20 | ETH | DOWN | 0.65 | 0.87 | 1.96 |
| 11-01 04:31 | +15 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 11-01 04:31 | +10 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
