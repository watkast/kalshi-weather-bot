# Range-Scalp Bot

*Updated Thu Oct 29 16:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39414 | 34408 | 5006 (50) | 5 | $-10963.52 | -4.4% |
| **+10¢** | 29381 | 23596 | 5785 (73) | 6 | $-9707.94 | -5.3% |
| **+15¢** | 24563 | 18347 | 6216 (100) | 7 | $-8665.65 | -5.6% |
| **+20¢** | 21794 | 15282 | 6512 (129) | 7 | $-7554.14 | -5.5% |
| **+10¢ (15¢ stop)** | 48155 | 48085 | 70 (37) | 2 | $-18265.45 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 16:07 | +5 | BTC | UP | 0.68 | open |  |
| 10-29 16:07 | +10 stop | XRP | UP | 0.69 | open |  |
| 10-29 16:07 | +5 | XRP | UP | 0.68 | 0.74 | 0.30 |
| 10-29 16:06 | +10 stop | BTC | UP | 0.67 | open |  |
| 10-29 16:06 | +15 | BTC | UP | 0.67 | open |  |
| 10-29 16:06 | +10 stop | NEAR | UP | 0.65 | 0.77 | 0.91 |
| 10-29 16:06 | +5 | SOL | UP | 0.63 | 0.77 | 1.10 |
| 10-29 16:06 | +10 | BTC | UP | 0.63 | open |  |
| 10-29 16:06 | +5 | BTC | UP | 0.63 | 0.69 | 0.28 |
| 10-29 16:05 | +10 stop | ETH | DOWN | 0.57 | 0.41 | -1.95 |
| 10-29 16:05 | +10 | ETH | DOWN | 0.56 | open |  |
| 10-29 16:05 | +5 | ETH | DOWN | 0.56 | open |  |
| 10-29 16:05 | +5 | XRP | DOWN | 0.57 | 0.69 | 0.87 |
| 10-29 16:05 | +10 stop | SOL | DOWN | 0.48 | 0.22 | -2.91 |
| 10-29 16:05 | +10 | SOL | DOWN | 0.50 | open |  |
| 10-29 16:05 | +5 | SOL | DOWN | 0.51 | 0.57 | 0.24 |
| 10-29 16:05 | +10 stop | BTC | UP | 0.52 | 0.67 | 1.16 |
| 10-29 16:05 | +20 | BTC | UP | 0.52 | open |  |
| 10-29 16:05 | +15 | BTC | UP | 0.52 | 0.67 | 1.16 |
| 10-29 16:05 | +10 | BTC | UP | 0.51 | 0.61 | 0.65 |
| 10-29 16:05 | +5 | BTC | UP | 0.51 | 0.61 | 0.65 |
| 10-29 16:04 | +10 stop | DOGE | UP | 0.66 | 0.39 | -3.03 |
| 10-29 16:04 | +10 | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 10-29 16:04 | +5 | DOGE | UP | 0.66 | 0.72 | 0.29 |
| 10-29 16:04 | +10 stop | ZEC | UP | 0.66 | 0.87 | 1.87 |
| 10-29 16:04 | +10 stop | SOL | DOWN | 0.49 | 0.62 | 0.96 |
| 10-29 16:04 | +15 | SOL | DOWN | 0.49 | open |  |
| 10-29 16:04 | +10 | SOL | DOWN | 0.50 | 0.62 | 0.85 |
| 10-29 16:04 | +5 | SOL | DOWN | 0.50 | 0.62 | 0.85 |
| 10-29 16:04 | +5 | XRP | DOWN | 0.54 | 0.68 | 1.06 |
| 10-29 16:04 | +10 stop | ETH | DOWN | 0.59 | 0.69 | 0.68 |
| 10-29 16:04 | +15 | ETH | DOWN | 0.59 | open |  |
| 10-29 16:04 | +10 | ETH | DOWN | 0.59 | 0.69 | 0.68 |
| 10-29 16:04 | +5 | ETH | DOWN | 0.59 | 0.69 | 0.68 |
| 10-29 16:04 | +10 stop | BNB | UP | 0.60 | 0.73 | 0.99 |
| 10-29 16:04 | +10 stop | NEAR | DOWN | 0.61 | 0.40 | -2.44 |
| 10-29 16:04 | +10 | NEAR | DOWN | 0.61 | open |  |
| 10-29 16:04 | +5 | NEAR | DOWN | 0.61 | open |  |
| 10-29 16:04 | +10 stop | XRP | DOWN | 0.60 | 0.43 | -2.05 |
| 10-29 16:04 | +15 | XRP | DOWN | 0.60 | open |  |
