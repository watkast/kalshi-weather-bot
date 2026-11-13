# Range-Scalp Bot

*Updated Fri Nov 13 02:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57674 | 50300 | 7374 (101) | 0 | $-15722.81 | -4.3% |
| **+10¢** | 43101 | 34489 | 8612 (133) | 2 | $-14670.16 | -5.4% |
| **+15¢** | 36140 | 26872 | 9268 (167) | 2 | $-13203.33 | -5.8% |
| **+20¢** | 32195 | 22469 | 9726 (217) | 2 | $-11579.32 | -5.7% |
| **+10¢ (15¢ stop)** | 70307 | 70179 | 128 (78) | 2 | $-25902.96 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 02:33 | +10 stop | HYPE | DOWN | 0.64 | open |  |
| 11-13 02:33 | +20 | HYPE | DOWN | 0.64 | open |  |
| 11-13 02:33 | +15 | HYPE | DOWN | 0.64 | open |  |
| 11-13 02:33 | +10 | HYPE | DOWN | 0.64 | open |  |
| 11-13 02:33 | +5 | HYPE | DOWN | 0.64 | 0.69 | 0.18 |
| 11-13 02:31 | +10 stop | XRP | DOWN | 0.68 | open |  |
| 11-13 02:31 | +20 | XRP | DOWN | 0.69 | open |  |
| 11-13 02:31 | +15 | XRP | DOWN | 0.69 | open |  |
| 11-13 02:31 | +10 | XRP | DOWN | 0.69 | open |  |
| 11-13 02:31 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 11-13 02:31 | +5 | ZEC | DOWN | 0.61 | 0.72 | 0.78 |
| 11-13 02:30 | +10 stop | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 11-13 02:30 | +20 | NEAR | DOWN | 0.60 | 0.82 | 1.92 |
| 11-13 02:30 | +15 | NEAR | DOWN | 0.60 | 0.77 | 1.40 |
| 11-13 02:30 | +10 | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 11-13 02:30 | +5 | NEAR | DOWN | 0.60 | 0.67 | 0.37 |
| 11-13 02:30 | +10 stop | BNB | DOWN | 0.68 | 0.86 | 1.55 |
| 11-13 02:30 | +20 | BNB | DOWN | 0.68 | 0.89 | 1.87 |
| 11-13 02:30 | +15 | BNB | DOWN | 0.68 | 0.86 | 1.55 |
| 11-13 02:30 | +10 | BNB | DOWN | 0.68 | 0.86 | 1.55 |
| 11-13 02:30 | +5 | BNB | DOWN | 0.68 | 0.86 | 1.55 |
| 11-13 02:30 | +10 stop | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 11-13 02:30 | +20 | DOGE | DOWN | 0.66 | 0.86 | 1.75 |
| 11-13 02:30 | +15 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-13 02:30 | +10 | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 11-13 02:30 | +5 | DOGE | DOWN | 0.66 | 0.73 | 0.40 |
| 11-13 02:30 | +10 stop | ZEC | DOWN | 0.57 | 0.72 | 1.17 |
| 11-13 02:30 | +20 | ZEC | DOWN | 0.57 | 0.83 | 2.32 |
| 11-13 02:30 | +15 | ZEC | DOWN | 0.57 | 0.72 | 1.17 |
| 11-13 02:30 | +10 | ZEC | DOWN | 0.57 | 0.72 | 1.17 |
| 11-13 02:30 | +5 | ZEC | DOWN | 0.57 | 0.62 | 0.15 |
| 11-13 02:28 | +15 | BTC | DOWN | 0.70 | 0.94 | 2.21 |
| 11-13 02:28 | +5 | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-13 02:27 | +10 stop | XRP | UP | 0.66 | 0.90 | 2.23 |
| 11-13 02:27 | +10 stop | ZEC | DOWN | 0.62 | 0.25 | -4.00 |
| 11-13 02:27 | +20 | ZEC | DOWN | 0.60 | yes | -6.22 |
| 11-13 02:27 | +5 | ZEC | DOWN | 0.61 | yes | -6.31 |
| 11-13 02:27 | +10 stop | SOL | DOWN | 0.68 | 0.29 | -4.21 |
| 11-13 02:27 | +20 | SOL | DOWN | 0.68 | yes | -6.96 |
| 11-13 02:27 | +15 | SOL | DOWN | 0.68 | yes | -6.96 |
