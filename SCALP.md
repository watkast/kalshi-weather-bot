# Range-Scalp Bot

*Updated Sun Oct 04 05:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1841 | 1581 | 260 (3) | 0 | $-661.73 | -5.7% |
| **+10¢** | 1432 | 1144 | 288 (4) | 0 | $-494.80 | -5.5% |
| **+15¢** | 1205 | 900 | 305 (5) | 0 | $-435.62 | -5.7% |
| **+20¢** | 1063 | 739 | 324 (7) | 0 | $-430.28 | -6.4% |
| **+10¢ (15¢ stop)** | 2321 | 2320 | 1 (1) | 0 | $-957.97 | -6.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 05:58 | +10 | BTC | DOWN | 0.68 | 0.81 | 1.03 |
| 10-04 05:58 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 10-04 05:56 | +10 stop | BTC | DOWN | 0.68 | 0.81 | 1.03 |
| 10-04 05:56 | +10 stop | BTC | DOWN | 0.34 | 0.64 | 2.67 |
| 10-04 05:54 | +10 stop | BTC | UP | 0.69 | 0.80 | 0.83 |
| 10-04 05:52 | +5 | BTC | DOWN | 0.66 | 0.72 | 0.29 |
| 10-04 05:51 | +10 stop | BNB | UP | 0.62 | 0.75 | 1.00 |
| 10-04 05:49 | +5 | BTC | DOWN | 0.64 | 0.70 | 0.28 |
| 10-04 05:48 | +5 | BNB | DOWN | 0.66 | 0.72 | 0.29 |
| 10-04 05:46 | +10 stop | BTC | DOWN | 0.62 | 0.33 | -3.23 |
| 10-04 05:46 | +20 | BTC | DOWN | 0.62 | 0.94 | 3.04 |
| 10-04 05:46 | +15 | BTC | DOWN | 0.62 | 0.81 | 1.62 |
| 10-04 05:46 | +10 | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-04 05:46 | +5 | BTC | DOWN | 0.62 | 0.71 | 0.58 |
| 10-04 05:46 | +10 stop | ETH | DOWN | 0.65 | 0.84 | 1.64 |
| 10-04 05:46 | +20 | ETH | DOWN | 0.65 | 0.87 | 1.96 |
| 10-04 05:46 | +15 | ETH | DOWN | 0.65 | 0.84 | 1.64 |
| 10-04 05:46 | +10 | ETH | DOWN | 0.65 | 0.84 | 1.64 |
| 10-04 05:46 | +5 | ETH | DOWN | 0.65 | 0.71 | 0.29 |
| 10-04 05:46 | +10 stop | BNB | DOWN | 0.70 | 0.48 | -2.53 |
| 10-04 05:46 | +20 | BNB | DOWN | 0.70 | 0.98 | 2.63 |
| 10-04 05:46 | +15 | BNB | DOWN | 0.70 | 0.98 | 2.63 |
| 10-04 05:46 | +10 | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 10-04 05:46 | +5 | BNB | DOWN | 0.70 | 0.77 | 0.42 |
| 10-04 05:46 | +10 stop | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-04 05:46 | +20 | XRP | DOWN | 0.67 | 0.89 | 1.93 |
| 10-04 05:46 | +15 | XRP | DOWN | 0.67 | 0.83 | 1.30 |
| 10-04 05:46 | +10 | XRP | DOWN | 0.67 | 0.78 | 0.77 |
| 10-04 05:46 | +5 | XRP | DOWN | 0.67 | 0.74 | 0.36 |
| 10-04 05:40 | +10 stop | ETH | DOWN | 0.63 | 0.46 | -2.04 |
| 10-04 05:37 | +10 stop | BNB | DOWN | 0.60 | 0.38 | -2.59 |
| 10-04 05:37 | +20 | BNB | DOWN | 0.61 | yes | -6.27 |
| 10-04 05:37 | +15 | BNB | DOWN | 0.61 | yes | -6.27 |
| 10-04 05:37 | +10 | BNB | DOWN | 0.61 | yes | -6.27 |
| 10-04 05:37 | +5 | BNB | DOWN | 0.61 | yes | -6.27 |
| 10-04 05:37 | +10 stop | ETH | UP | 0.55 | 0.36 | -2.25 |
| 10-04 05:37 | +10 | ETH | UP | 0.55 | 0.80 | 2.20 |
| 10-04 05:37 | +5 | ETH | UP | 0.55 | 0.80 | 2.20 |
| 10-04 05:37 | +10 stop | HYPE | UP | 0.65 | 0.83 | 1.54 |
| 10-04 05:36 | +10 stop | DOGE | UP | 0.57 | 0.83 | 2.28 |
