# Range-Scalp Bot

*Updated Sat Oct 10 09:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10208 | 8799 | 1409 (22) | 3 | $-3489.05 | -5.4% |
| **+10¢** | 7717 | 6077 | 1640 (34) | 2 | $-3345.34 | -6.9% |
| **+15¢** | 6515 | 4781 | 1734 (49) | 4 | $-2796.25 | -6.8% |
| **+20¢** | 5789 | 3985 | 1804 (63) | 3 | $-2363.19 | -6.5% |
| **+10¢ (15¢ stop)** | 12541 | 12504 | 37 (24) | 0 | $-4930.89 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 09:10 | +10 stop | DOGE | UP | 0.56 | 0.68 | 0.86 |
| 10-10 09:10 | +10 stop | HYPE | UP | 0.60 | 0.78 | 1.50 |
| 10-10 09:10 | +20 | HYPE | UP | 0.60 | 0.83 | 2.03 |
| 10-10 09:10 | +10 | HYPE | UP | 0.60 | 0.78 | 1.50 |
| 10-10 09:10 | +5 | HYPE | UP | 0.60 | 0.68 | 0.47 |
| 10-10 09:08 | +10 stop | DOGE | DOWN | 0.60 | 0.39 | -2.44 |
| 10-10 09:08 | +15 | DOGE | DOWN | 0.60 | open |  |
| 10-10 09:08 | +10 | DOGE | DOWN | 0.60 | open |  |
| 10-10 09:08 | +5 | DOGE | DOWN | 0.60 | open |  |
| 10-10 09:08 | +10 stop | BNB | UP | 0.55 | 0.73 | 1.48 |
| 10-10 09:08 | +10 | BNB | UP | 0.55 | 0.73 | 1.48 |
| 10-10 09:08 | +10 stop | XRP | UP | 0.65 | 0.46 | -2.24 |
| 10-10 09:07 | +10 stop | BNB | DOWN | 0.55 | 0.68 | 0.96 |
| 10-10 09:07 | +10 | BNB | DOWN | 0.55 | 0.68 | 0.96 |
| 10-10 09:07 | +5 | BNB | DOWN | 0.69 | open |  |
| 10-10 09:07 | +10 stop | ETH | DOWN | 0.57 | 0.41 | -1.95 |
| 10-10 09:06 | +10 stop | HYPE | UP | 0.61 | 0.73 | 0.89 |
| 10-10 09:06 | +15 | HYPE | UP | 0.61 | 0.78 | 1.40 |
| 10-10 09:06 | +10 | HYPE | UP | 0.61 | 0.73 | 0.89 |
| 10-10 09:06 | +5 | HYPE | UP | 0.61 | 0.70 | 0.58 |
| 10-10 09:06 | +10 stop | NEAR | UP | 0.58 | 0.42 | -1.95 |
| 10-10 09:06 | +15 | NEAR | UP | 0.59 | open |  |
| 10-10 09:06 | +10 | NEAR | UP | 0.59 | open |  |
| 10-10 09:06 | +15 | SOL | UP | 0.63 | 0.80 | 1.38 |
| 10-10 09:05 | +10 stop | BNB | DOWN | 0.55 | 0.68 | 0.97 |
| 10-10 09:05 | +15 | BNB | DOWN | 0.55 | open |  |
| 10-10 09:05 | +10 | BNB | DOWN | 0.55 | 0.68 | 0.97 |
| 10-10 09:05 | +5 | BNB | DOWN | 0.55 | 0.60 | 0.16 |
| 10-10 09:05 | +10 stop | BNB | UP | 0.45 | 0.64 | 1.55 |
| 10-10 09:05 | +10 | BNB | UP | 0.45 | 0.64 | 1.55 |
| 10-10 09:05 | +10 | ETH | UP | 0.64 | 0.77 | 1.00 |
| 10-10 09:05 | +5 | ETH | UP | 0.64 | 0.77 | 1.00 |
| 10-10 09:05 | +10 | SOL | UP | 0.63 | 0.73 | 0.69 |
| 10-10 09:05 | +10 stop | XRP | UP | 0.63 | 0.45 | -2.15 |
| 10-10 09:05 | +10 | XRP | UP | 0.63 | 0.85 | 1.94 |
| 10-10 09:05 | +5 | XRP | UP | 0.63 | 0.69 | 0.28 |
| 10-10 09:05 | +10 stop | SOL | UP | 0.64 | 0.76 | 0.90 |
| 10-10 09:05 | +5 | DOGE | DOWN | 0.59 | 0.73 | 1.09 |
| 10-10 09:05 | +5 | NEAR | DOWN | 0.59 | 0.69 | 0.64 |
| 10-10 09:05 | +10 stop | ETH | UP | 0.64 | 0.41 | -2.64 |
