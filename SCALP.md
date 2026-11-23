# Range-Scalp Bot

*Updated Mon Nov 23 13:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70057 | 61138 | 8919 (146) | 0 | $-18822.68 | -4.3% |
| **+10¢** | 52268 | 41850 | 10418 (189) | 0 | $-17483.27 | -5.3% |
| **+15¢** | 43799 | 32578 | 11221 (245) | 0 | $-15581.44 | -5.7% |
| **+20¢** | 38996 | 27188 | 11808 (310) | 0 | $-13943.03 | -5.7% |
| **+10¢ (15¢ stop)** | 85332 | 85142 | 190 (118) | 0 | $-31349.17 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 13:40 | +10 stop | BNB | DOWN | 0.50 | 0.73 | 1.99 |
| 11-23 13:40 | +10 stop | ETH | DOWN | 0.59 | 0.72 | 0.98 |
| 11-23 13:40 | +10 | ETH | DOWN | 0.58 | 0.72 | 1.07 |
| 11-23 13:40 | +5 | ETH | DOWN | 0.57 | 0.72 | 1.17 |
| 11-23 13:40 | +10 stop | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-23 13:40 | +20 | BTC | DOWN | 0.65 | 0.85 | 1.75 |
| 11-23 13:40 | +15 | BTC | DOWN | 0.65 | 0.82 | 1.43 |
| 11-23 13:40 | +10 | BTC | DOWN | 0.66 | 0.82 | 1.33 |
| 11-23 13:40 | +5 | BTC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-23 13:38 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
| 11-23 13:37 | +10 stop | BNB | DOWN | 0.69 | 0.42 | -3.03 |
| 11-23 13:37 | +20 | BNB | DOWN | 0.69 | 0.99 | 2.86 |
| 11-23 13:37 | +15 | BNB | DOWN | 0.69 | 0.99 | 2.86 |
| 11-23 13:37 | +10 | BNB | DOWN | 0.69 | 0.99 | 2.86 |
| 11-23 13:37 | +5 | BNB | DOWN | 0.69 | 0.76 | 0.42 |
| 11-23 13:37 | +10 stop | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 11-23 13:37 | +20 | ETH | DOWN | 0.66 | 0.88 | 1.96 |
| 11-23 13:37 | +15 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 11-23 13:37 | +10 | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 11-23 13:37 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
| 11-23 13:34 | +15 | NEAR | DOWN | 0.70 | 0.91 | 1.93 |
| 11-23 13:34 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-23 13:34 | +5 | NEAR | DOWN | 0.70 | 0.75 | 0.21 |
| 11-23 13:33 | +10 stop | NEAR | DOWN | 0.71 | 0.83 | 0.95 |
| 11-23 13:31 | +10 stop | BNB | DOWN | 0.66 | 0.79 | 1.03 |
| 11-23 13:31 | +20 | BNB | DOWN | 0.65 | 0.85 | 1.75 |
| 11-23 13:31 | +15 | BNB | DOWN | 0.65 | 0.81 | 1.33 |
| 11-23 13:31 | +10 | BNB | DOWN | 0.65 | 0.79 | 1.12 |
| 11-23 13:31 | +5 | BNB | DOWN | 0.65 | 0.79 | 1.12 |
| 11-23 13:31 | +10 stop | NEAR | DOWN | 0.58 | 0.74 | 1.28 |
| 11-23 13:31 | +20 | NEAR | DOWN | 0.58 | 0.78 | 1.69 |
| 11-23 13:31 | +15 | NEAR | DOWN | 0.58 | 0.74 | 1.28 |
| 11-23 13:31 | +10 | NEAR | DOWN | 0.58 | 0.74 | 1.29 |
| 11-23 13:31 | +5 | NEAR | DOWN | 0.58 | 0.74 | 1.29 |
| 11-23 13:28 | +10 stop | BNB | UP | 0.13 | 0.59 | 4.40 |
| 11-23 13:27 | +10 stop | XRP | UP | 0.70 | 0.55 | -1.83 |
| 11-23 13:26 | +10 stop | DOGE | UP | 0.57 | 0.81 | 2.11 |
| 11-23 13:26 | +10 stop | HYPE | UP | 0.55 | 0.78 | 1.99 |
| 11-23 13:26 | +5 | DOGE | UP | 0.58 | 0.66 | 0.46 |
| 11-23 13:26 | +5 | ETH | DOWN | 0.55 | yes | -5.68 |
