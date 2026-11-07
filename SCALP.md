# Range-Scalp Bot

*Updated Sat Nov 07 01:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50256 | 43812 | 6444 (76) | 1 | $-14098.27 | -4.5% |
| **+10¢** | 37502 | 30001 | 7501 (102) | 2 | $-13013.72 | -5.5% |
| **+15¢** | 31407 | 23323 | 8084 (131) | 2 | $-11927.37 | -6.1% |
| **+20¢** | 27920 | 19444 | 8476 (173) | 2 | $-10548.40 | -6.0% |
| **+10¢ (15¢ stop)** | 61185 | 61086 | 99 (58) | 0 | $-22657.36 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 01:13 | +10 stop | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-07 01:13 | +10 | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-07 01:13 | +5 | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-07 01:12 | +10 stop | BTC | UP | 0.58 | 0.73 | 1.18 |
| 11-07 01:12 | +10 | BTC | UP | 0.58 | 0.73 | 1.18 |
| 11-07 01:12 | +5 | BTC | UP | 0.58 | 0.73 | 1.18 |
| 11-07 01:11 | +10 stop | BTC | UP | 0.54 | 0.67 | 0.96 |
| 11-07 01:11 | +20 | BTC | UP | 0.54 | 0.85 | 2.83 |
| 11-07 01:11 | +15 | BTC | UP | 0.54 | 0.73 | 1.58 |
| 11-07 01:11 | +10 | BTC | UP | 0.54 | 0.67 | 0.96 |
| 11-07 01:11 | +5 | BTC | UP | 0.54 | 0.67 | 0.96 |
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
| 11-07 01:00 | +20 | XRP | DOWN | 0.51 | 0.75 | 2.08 |
| 11-07 01:00 | +15 | XRP | DOWN | 0.51 | 0.75 | 2.08 |
| 11-07 01:00 | +10 | XRP | DOWN | 0.51 | 0.62 | 0.75 |
| 11-07 01:00 | +5 | XRP | DOWN | 0.51 | 0.62 | 0.75 |
| 11-07 00:58 | +10 stop | BTC | DOWN | 0.55 | 0.71 | 1.27 |
| 11-07 00:57 | +5 | SOL | UP | 0.58 | 0.79 | 1.80 |
| 11-07 00:56 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
