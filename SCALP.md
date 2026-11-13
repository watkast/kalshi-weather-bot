# Range-Scalp Bot

*Updated Fri Nov 13 10:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58115 | 50709 | 7406 (102) | 0 | $-15686.61 | -4.3% |
| **+10¢** | 43419 | 34758 | 8661 (134) | 0 | $-14663.57 | -5.4% |
| **+15¢** | 36401 | 27076 | 9325 (168) | 1 | $-13228.39 | -5.8% |
| **+20¢** | 32431 | 22642 | 9789 (219) | 2 | $-11596.69 | -5.7% |
| **+10¢ (15¢ stop)** | 70803 | 70674 | 129 (79) | 0 | $-26027.06 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 10:03 | +5 | HYPE | UP | 0.66 | 0.72 | 0.29 |
| 11-13 10:02 | +10 stop | HYPE | UP | 0.54 | 0.68 | 1.06 |
| 11-13 10:02 | +20 | HYPE | UP | 0.54 | open |  |
| 11-13 10:02 | +15 | HYPE | UP | 0.54 | 0.72 | 1.47 |
| 11-13 10:02 | +10 | HYPE | UP | 0.54 | 0.68 | 1.11 |
| 11-13 10:02 | +5 | HYPE | UP | 0.54 | 0.61 | 0.35 |
| 11-13 10:02 | +10 stop | ETH | UP | 0.66 | 0.76 | 0.71 |
| 11-13 10:02 | +20 | ETH | UP | 0.66 | 0.88 | 1.96 |
| 11-13 10:02 | +15 | ETH | UP | 0.66 | 0.85 | 1.65 |
| 11-13 10:02 | +10 | ETH | UP | 0.66 | 0.76 | 0.71 |
| 11-13 10:02 | +5 | ETH | UP | 0.66 | 0.72 | 0.29 |
| 11-13 10:02 | +10 stop | BTC | UP | 0.63 | 0.75 | 0.89 |
| 11-13 10:02 | +15 | BTC | UP | 0.63 | 0.78 | 1.20 |
| 11-13 10:02 | +10 | BTC | UP | 0.63 | 0.75 | 0.89 |
| 11-13 10:02 | +10 stop | XRP | UP | 0.65 | 0.79 | 1.12 |
| 11-13 10:02 | +20 | XRP | UP | 0.65 | open |  |
| 11-13 10:02 | +15 | XRP | UP | 0.65 | open |  |
| 11-13 10:02 | +10 | XRP | UP | 0.65 | 0.79 | 1.12 |
| 11-13 10:02 | +5 | XRP | UP | 0.65 | 0.72 | 0.39 |
| 11-13 10:01 | +5 | BTC | UP | 0.68 | 0.75 | 0.40 |
| 11-13 10:00 | +10 stop | BTC | UP | 0.55 | 0.72 | 1.37 |
| 11-13 10:00 | +20 | BTC | UP | 0.55 | 0.75 | 1.68 |
| 11-13 10:00 | +15 | BTC | UP | 0.55 | 0.72 | 1.37 |
| 11-13 10:00 | +10 | BTC | UP | 0.55 | 0.72 | 1.37 |
| 11-13 10:00 | +5 | BTC | UP | 0.55 | 0.61 | 0.25 |
| 11-13 09:58 | +10 stop | DOGE | UP | 0.69 | 0.97 | 2.58 |
| 11-13 09:58 | +10 | DOGE | UP | 0.68 | 0.97 | 2.68 |
| 11-13 09:58 | +5 | DOGE | UP | 0.68 | 0.97 | 2.67 |
| 11-13 09:58 | +10 stop | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 11-13 09:58 | +5 | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 11-13 09:57 | +10 stop | DOGE | DOWN | 0.48 | 0.63 | 1.15 |
| 11-13 09:57 | +20 | DOGE | DOWN | 0.49 | yes | -5.08 |
| 11-13 09:57 | +15 | DOGE | DOWN | 0.49 | yes | -5.08 |
| 11-13 09:57 | +10 | DOGE | DOWN | 0.49 | 0.63 | 1.05 |
| 11-13 09:57 | +5 | DOGE | DOWN | 0.48 | 0.63 | 1.15 |
| 11-13 09:56 | +5 | ETH | UP | 0.65 | 0.71 | 0.29 |
| 11-13 09:55 | +10 stop | HYPE | DOWN | 0.67 | 0.81 | 1.13 |
| 11-13 09:55 | +10 stop | DOGE | DOWN | 0.64 | 0.80 | 1.31 |
| 11-13 09:55 | +10 | DOGE | DOWN | 0.63 | 0.80 | 1.40 |
| 11-13 09:55 | +10 stop | ETH | DOWN | 0.47 | 0.27 | -2.33 |
