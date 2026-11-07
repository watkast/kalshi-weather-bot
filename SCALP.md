# Range-Scalp Bot

*Updated Sat Nov 07 01:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50253 | 43809 | 6444 (76) | 1 | $-14101.11 | -4.5% |
| **+10¢** | 37499 | 29998 | 7501 (102) | 2 | $-13016.56 | -5.5% |
| **+15¢** | 31405 | 23321 | 8084 (131) | 3 | $-11931.03 | -6.1% |
| **+20¢** | 27918 | 19442 | 8476 (173) | 3 | $-10553.31 | -6.0% |
| **+10¢ (15¢ stop)** | 61182 | 61083 | 99 (58) | 0 | $-22660.20 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 01:06 | +10 stop | BNB | UP | 0.64 | 0.75 | 0.79 |
| 11-07 01:06 | +5 | BNB | UP | 0.64 | 0.75 | 0.79 |
| 11-07 01:05 | +10 stop | XRP | UP | 0.63 | 0.74 | 0.79 |
| 11-07 01:05 | +10 | XRP | UP | 0.63 | 0.74 | 0.79 |
| 11-07 01:05 | +5 | XRP | UP | 0.63 | 0.71 | 0.48 |
| 11-07 01:05 | +10 stop | HYPE | UP | 0.67 | 0.31 | -3.91 |
| 11-07 01:05 | +20 | HYPE | UP | 0.67 | open |  |
| 11-07 01:05 | +15 | HYPE | UP | 0.67 | open |  |
| 11-07 01:05 | +10 | HYPE | UP | 0.67 | open |  |
| 11-07 01:05 | +5 | HYPE | UP | 0.67 | open |  |
| 11-07 01:01 | +5 | BNB | UP | 0.58 | 0.73 | 1.18 |
| 11-07 01:01 | +10 stop | BNB | DOWN | 0.47 | 0.24 | -2.61 |
| 11-07 01:01 | +20 | BNB | DOWN | 0.47 | open |  |
| 11-07 01:01 | +15 | BNB | DOWN | 0.47 | open |  |
| 11-07 01:01 | +10 | BNB | DOWN | 0.47 | open |  |
| 11-07 01:01 | +5 | BNB | DOWN | 0.47 | 0.56 | 0.54 |
| 11-07 01:00 | +10 stop | NEAR | UP | 0.71 | 0.81 | 0.74 |
| 11-07 01:00 | +20 | NEAR | UP | 0.71 | 0.95 | 2.21 |
| 11-07 01:00 | +15 | NEAR | UP | 0.71 | 0.86 | 1.26 |
| 11-07 01:00 | +10 | NEAR | UP | 0.71 | 0.81 | 0.74 |
| 11-07 01:00 | +5 | NEAR | UP | 0.71 | 0.76 | 0.22 |
| 11-07 01:00 | +10 stop | XRP | DOWN | 0.51 | 0.62 | 0.75 |
| 11-07 01:00 | +20 | XRP | DOWN | 0.51 | open |  |
| 11-07 01:00 | +15 | XRP | DOWN | 0.51 | open |  |
| 11-07 01:00 | +10 | XRP | DOWN | 0.51 | 0.62 | 0.75 |
| 11-07 01:00 | +5 | XRP | DOWN | 0.51 | 0.62 | 0.75 |
| 11-07 00:58 | +10 stop | BTC | DOWN | 0.55 | 0.71 | 1.27 |
| 11-07 00:57 | +5 | SOL | UP | 0.58 | 0.79 | 1.80 |
| 11-07 00:56 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-07 00:56 | +10 | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-07 00:56 | +5 | ETH | DOWN | 0.65 | 0.70 | 0.19 |
| 11-07 00:56 | +10 stop | XRP | DOWN | 0.58 | 0.87 | 2.64 |
| 11-07 00:56 | +20 | XRP | DOWN | 0.59 | 0.87 | 2.55 |
| 11-07 00:56 | +15 | XRP | DOWN | 0.55 | 0.87 | 2.94 |
| 11-07 00:56 | +10 | XRP | DOWN | 0.55 | 0.65 | 0.66 |
| 11-07 00:56 | +5 | XRP | DOWN | 0.55 | 0.65 | 0.66 |
| 11-07 00:55 | +10 stop | ETH | DOWN | 0.58 | 0.69 | 0.77 |
| 11-07 00:55 | +20 | ETH | DOWN | 0.58 | 0.82 | 2.11 |
| 11-07 00:55 | +15 | ETH | DOWN | 0.58 | 0.74 | 1.28 |
| 11-07 00:55 | +10 | ETH | DOWN | 0.58 | 0.69 | 0.77 |
