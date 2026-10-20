# Range-Scalp Bot

*Updated Tue Oct 20 03:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25017 | 21780 | 3237 (31) | 1 | $-7324.72 | -4.6% |
| **+10¢** | 18821 | 15083 | 3738 (46) | 1 | $-6492.81 | -5.5% |
| **+15¢** | 15749 | 11723 | 4026 (70) | 2 | $-5851.47 | -5.9% |
| **+20¢** | 13922 | 9707 | 4215 (88) | 5 | $-5258.61 | -6.0% |
| **+10¢ (15¢ stop)** | 30698 | 30646 | 52 (30) | 1 | $-11422.03 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 03:19 | +5 | BNB | DOWN | 0.54 | 0.60 | 0.25 |
| 10-20 03:17 | +5 | NEAR | DOWN | 0.66 | open |  |
| 10-20 03:17 | +10 stop | BNB | DOWN | 0.58 | open |  |
| 10-20 03:17 | +20 | BNB | DOWN | 0.58 | open |  |
| 10-20 03:17 | +15 | BNB | DOWN | 0.58 | open |  |
| 10-20 03:17 | +10 | BNB | DOWN | 0.58 | open |  |
| 10-20 03:17 | +5 | BNB | DOWN | 0.58 | 0.64 | 0.25 |
| 10-20 03:16 | +10 stop | NEAR | DOWN | 0.59 | 0.70 | 0.78 |
| 10-20 03:16 | +20 | NEAR | DOWN | 0.59 | open |  |
| 10-20 03:16 | +15 | NEAR | DOWN | 0.59 | open |  |
| 10-20 03:16 | +10 | NEAR | DOWN | 0.57 | 0.67 | 0.66 |
| 10-20 03:16 | +5 | NEAR | DOWN | 0.57 | 0.62 | 0.15 |
| 10-20 03:16 | +10 stop | ETH | DOWN | 0.63 | 0.79 | 1.31 |
| 10-20 03:16 | +20 | ETH | DOWN | 0.63 | open |  |
| 10-20 03:16 | +15 | ETH | DOWN | 0.63 | 0.79 | 1.31 |
| 10-20 03:16 | +10 | ETH | DOWN | 0.63 | 0.79 | 1.31 |
| 10-20 03:16 | +5 | ETH | DOWN | 0.63 | 0.71 | 0.48 |
| 10-20 03:16 | +10 stop | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-20 03:16 | +20 | HYPE | DOWN | 0.64 | 0.86 | 1.94 |
| 10-20 03:16 | +15 | HYPE | DOWN | 0.64 | 0.83 | 1.63 |
| 10-20 03:16 | +10 | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
| 10-20 03:16 | +5 | HYPE | DOWN | 0.62 | 0.68 | 0.27 |
| 10-20 03:16 | +10 stop | XRP | DOWN | 0.63 | 0.74 | 0.79 |
| 10-20 03:16 | +20 | XRP | DOWN | 0.63 | open |  |
| 10-20 03:16 | +15 | XRP | DOWN | 0.63 | 0.79 | 1.31 |
| 10-20 03:16 | +10 | XRP | DOWN | 0.63 | 0.74 | 0.79 |
| 10-20 03:16 | +5 | XRP | DOWN | 0.63 | 0.74 | 0.79 |
| 10-20 03:16 | +10 stop | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 10-20 03:16 | +10 | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 10-20 03:16 | +10 stop | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-20 03:16 | +20 | DOGE | DOWN | 0.66 | open |  |
| 10-20 03:16 | +15 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-20 03:16 | +10 | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-20 03:16 | +5 | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-20 03:16 | +5 | ZEC | DOWN | 0.66 | 0.71 | 0.19 |
| 10-20 03:15 | +10 stop | SOL | DOWN | 0.61 | 0.72 | 0.78 |
| 10-20 03:15 | +20 | SOL | DOWN | 0.61 | 0.81 | 1.72 |
| 10-20 03:15 | +15 | SOL | DOWN | 0.61 | 0.76 | 1.20 |
| 10-20 03:15 | +10 | SOL | DOWN | 0.61 | 0.72 | 0.78 |
| 10-20 03:15 | +5 | SOL | DOWN | 0.61 | 0.72 | 0.78 |
