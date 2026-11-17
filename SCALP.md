# Range-Scalp Bot

*Updated Tue Nov 17 04:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62566 | 54583 | 7983 (117) | 1 | $-16954.86 | -4.3% |
| **+10¢** | 46728 | 37387 | 9341 (159) | 3 | $-15823.31 | -5.4% |
| **+15¢** | 39165 | 29090 | 10075 (201) | 5 | $-14371.24 | -5.8% |
| **+20¢** | 34909 | 24344 | 10565 (256) | 6 | $-12537.91 | -5.7% |
| **+10¢ (15¢ stop)** | 76145 | 75989 | 156 (92) | 3 | $-28042.48 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 04:34 | +10 stop | DOGE | DOWN | 0.64 | open |  |
| 11-17 04:34 | +10 | DOGE | DOWN | 0.64 | open |  |
| 11-17 04:34 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.18 |
| 11-17 04:34 | +10 stop | NEAR | DOWN | 0.62 | open |  |
| 11-17 04:34 | +10 | NEAR | DOWN | 0.62 | open |  |
| 11-17 04:34 | +5 | NEAR | DOWN | 0.62 | 0.67 | 0.17 |
| 11-17 04:34 | +5 | ETH | DOWN | 0.62 | open |  |
| 11-17 04:32 | +10 stop | ETH | DOWN | 0.67 | open |  |
| 11-17 04:32 | +10 | ETH | DOWN | 0.67 | open |  |
| 11-17 04:32 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 11-17 04:32 | +10 stop | BTC | DOWN | 0.67 | 0.80 | 1.02 |
| 11-17 04:32 | +20 | BTC | DOWN | 0.67 | open |  |
| 11-17 04:32 | +15 | BTC | DOWN | 0.67 | open |  |
| 11-17 04:32 | +10 | BTC | DOWN | 0.67 | 0.80 | 1.02 |
| 11-17 04:32 | +5 | BTC | DOWN | 0.67 | 0.76 | 0.61 |
| 11-17 04:31 | +10 stop | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-17 04:31 | +20 | HYPE | DOWN | 0.71 | open |  |
| 11-17 04:31 | +15 | HYPE | DOWN | 0.71 | 0.89 | 1.58 |
| 11-17 04:31 | +10 | HYPE | DOWN | 0.71 | 0.83 | 0.99 |
| 11-17 04:31 | +5 | HYPE | DOWN | 0.71 | 0.79 | 0.57 |
| 11-17 04:31 | +10 stop | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 11-17 04:31 | +20 | NEAR | DOWN | 0.66 | open |  |
| 11-17 04:31 | +15 | NEAR | DOWN | 0.66 | open |  |
| 11-17 04:31 | +10 | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 11-17 04:31 | +5 | NEAR | DOWN | 0.66 | 0.71 | 0.19 |
| 11-17 04:30 | +10 stop | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 11-17 04:30 | +20 | ETH | DOWN | 0.63 | open |  |
| 11-17 04:30 | +15 | ETH | DOWN | 0.63 | open |  |
| 11-17 04:30 | +10 | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 11-17 04:30 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.17 |
| 11-17 04:30 | +10 stop | DOGE | DOWN | 0.62 | 0.73 | 0.79 |
| 11-17 04:30 | +20 | DOGE | DOWN | 0.62 | open |  |
| 11-17 04:30 | +15 | DOGE | DOWN | 0.62 | open |  |
| 11-17 04:30 | +10 | DOGE | DOWN | 0.62 | 0.73 | 0.79 |
| 11-17 04:30 | +5 | DOGE | DOWN | 0.62 | 0.73 | 0.79 |
| 11-17 04:30 | +10 stop | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 11-17 04:30 | +20 | XRP | DOWN | 0.65 | open |  |
| 11-17 04:30 | +15 | XRP | DOWN | 0.65 | open |  |
| 11-17 04:30 | +10 | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-17 04:30 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
