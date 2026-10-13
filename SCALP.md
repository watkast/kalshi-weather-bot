# Range-Scalp Bot

*Updated Tue Oct 13 17:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14724 | 12738 | 1986 (27) | 3 | $-4734.69 | -5.1% |
| **+10¢** | 11138 | 8832 | 2306 (39) | 5 | $-4432.36 | -6.3% |
| **+15¢** | 9361 | 6891 | 2470 (57) | 5 | $-3970.86 | -6.8% |
| **+20¢** | 8327 | 5753 | 2574 (73) | 7 | $-3424.03 | -6.6% |
| **+10¢ (15¢ stop)** | 18084 | 18034 | 50 (29) | 4 | $-7056.71 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 17:38 | +5 | BTC | DOWN | 0.54 | 0.59 | 0.15 |
| 10-13 17:38 | +10 stop | SOL | DOWN | 0.59 | open |  |
| 10-13 17:38 | +10 stop | BTC | DOWN | 0.60 | open |  |
| 10-13 17:38 | +10 stop | HYPE | UP | 0.53 | open |  |
| 10-13 17:38 | +10 stop | NEAR | UP | 0.63 | open |  |
| 10-13 17:38 | +10 | NEAR | UP | 0.63 | open |  |
| 10-13 17:38 | +5 | NEAR | UP | 0.63 | open |  |
| 10-13 17:37 | +10 stop | DOGE | DOWN | 0.47 | 0.65 | 1.41 |
| 10-13 17:37 | +10 | DOGE | DOWN | 0.47 | 0.65 | 1.41 |
| 10-13 17:37 | +5 | DOGE | DOWN | 0.48 | 0.65 | 1.36 |
| 10-13 17:36 | +10 stop | BTC | DOWN | 0.56 | 0.40 | -1.95 |
| 10-13 17:36 | +10 stop | SOL | DOWN | 0.59 | 0.34 | -2.83 |
| 10-13 17:36 | +10 stop | HYPE | DOWN | 0.58 | 0.37 | -2.45 |
| 10-13 17:36 | +10 | BTC | DOWN | 0.59 | open |  |
| 10-13 17:36 | +5 | BTC | DOWN | 0.59 | 0.64 | 0.16 |
| 10-13 17:36 | +5 | BTC | UP | 0.43 | 0.64 | 1.75 |
| 10-13 17:36 | +10 stop | BNB | DOWN | 0.69 | 0.51 | -2.13 |
| 10-13 17:36 | +20 | BNB | DOWN | 0.69 | open |  |
| 10-13 17:36 | +15 | BNB | DOWN | 0.69 | open |  |
| 10-13 17:36 | +10 | BNB | DOWN | 0.69 | open |  |
| 10-13 17:36 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 10-13 17:36 | +10 stop | DOGE | DOWN | 0.58 | 0.70 | 0.88 |
| 10-13 17:36 | +20 | DOGE | DOWN | 0.59 | open |  |
| 10-13 17:36 | +15 | DOGE | DOWN | 0.59 | 0.74 | 1.19 |
| 10-13 17:36 | +10 | DOGE | DOWN | 0.59 | 0.70 | 0.78 |
| 10-13 17:36 | +5 | DOGE | DOWN | 0.59 | 0.70 | 0.78 |
| 10-13 17:35 | +20 | HYPE | DOWN | 0.66 | open |  |
| 10-13 17:35 | +15 | HYPE | DOWN | 0.66 | open |  |
| 10-13 17:35 | +5 | HYPE | DOWN | 0.66 | open |  |
| 10-13 17:35 | +10 stop | BTC | DOWN | 0.49 | 0.62 | 0.95 |
| 10-13 17:34 | +10 stop | SOL | DOWN | 0.66 | 0.47 | -2.24 |
| 10-13 17:33 | +20 | SOL | DOWN | 0.64 | open |  |
| 10-13 17:33 | +15 | SOL | DOWN | 0.64 | open |  |
| 10-13 17:33 | +5 | BNB | DOWN | 0.68 | 0.77 | 0.57 |
| 10-13 17:33 | +10 stop | SOL | DOWN | 0.71 | 0.53 | -2.13 |
| 10-13 17:33 | +10 | SOL | DOWN | 0.71 | open |  |
| 10-13 17:32 | +5 | SOL | DOWN | 0.71 | open |  |
| 10-13 17:32 | +10 stop | HYPE | DOWN | 0.66 | 0.47 | -2.22 |
| 10-13 17:32 | +10 | HYPE | DOWN | 0.66 | open |  |
| 10-13 17:32 | +5 | HYPE | DOWN | 0.66 | 0.72 | 0.31 |
