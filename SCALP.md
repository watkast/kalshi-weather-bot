# Range-Scalp Bot

*Updated Mon Oct 12 10:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13426 | 11614 | 1812 (25) | 3 | $-4293.43 | -5.1% |
| **+10¢** | 10166 | 8065 | 2101 (37) | 4 | $-4006.50 | -6.3% |
| **+15¢** | 8555 | 6309 | 2246 (55) | 4 | $-3523.51 | -6.6% |
| **+20¢** | 7615 | 5272 | 2343 (70) | 4 | $-3001.18 | -6.3% |
| **+10¢ (15¢ stop)** | 16514 | 16473 | 41 (25) | 4 | $-6441.17 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 10:19 | +10 stop | ETH | DOWN | 0.66 | open |  |
| 10-12 10:18 | +10 stop | NEAR | UP | 0.45 | open |  |
| 10-12 10:18 | +10 stop | BNB | DOWN | 0.70 | open |  |
| 10-12 10:18 | +20 | BNB | DOWN | 0.70 | open |  |
| 10-12 10:18 | +15 | BNB | DOWN | 0.70 | open |  |
| 10-12 10:18 | +10 | BNB | DOWN | 0.70 | open |  |
| 10-12 10:18 | +5 | BNB | DOWN | 0.70 | open |  |
| 10-12 10:17 | +10 stop | HYPE | UP | 0.64 | open |  |
| 10-12 10:16 | +10 stop | NEAR | DOWN | 0.61 | 0.45 | -1.95 |
| 10-12 10:16 | +20 | NEAR | DOWN | 0.61 | open |  |
| 10-12 10:16 | +15 | NEAR | DOWN | 0.61 | open |  |
| 10-12 10:16 | +10 | NEAR | DOWN | 0.61 | open |  |
| 10-12 10:16 | +5 | NEAR | DOWN | 0.61 | open |  |
| 10-12 10:16 | +10 stop | ETH | DOWN | 0.63 | 0.48 | -1.85 |
| 10-12 10:16 | +20 | ETH | DOWN | 0.63 | open |  |
| 10-12 10:16 | +15 | ETH | DOWN | 0.63 | open |  |
| 10-12 10:16 | +10 | ETH | DOWN | 0.63 | open |  |
| 10-12 10:16 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.17 |
| 10-12 10:16 | +10 stop | HYPE | DOWN | 0.63 | 0.45 | -2.15 |
| 10-12 10:16 | +20 | HYPE | DOWN | 0.63 | open |  |
| 10-12 10:16 | +15 | HYPE | DOWN | 0.63 | open |  |
| 10-12 10:16 | +10 | HYPE | DOWN | 0.63 | open |  |
| 10-12 10:16 | +5 | HYPE | DOWN | 0.63 | open |  |
| 10-12 10:10 | +10 stop | NEAR | UP | 0.51 | 0.25 | -2.92 |
| 10-12 10:08 | +10 stop | NEAR | DOWN | 0.66 | 0.41 | -2.83 |
| 10-12 10:07 | +10 stop | NEAR | DOWN | 0.58 | 0.68 | 0.66 |
| 10-12 10:06 | +10 stop | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-12 10:06 | +10 | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-12 10:06 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-12 10:05 | +10 stop | NEAR | DOWN | 0.71 | 0.56 | -1.83 |
| 10-12 10:05 | +10 | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 10-12 10:05 | +5 | NEAR | DOWN | 0.71 | 0.76 | 0.22 |
| 10-12 10:05 | +10 stop | BTC | DOWN | 0.66 | 0.82 | 1.33 |
| 10-12 10:05 | +10 | BTC | DOWN | 0.66 | 0.82 | 1.33 |
| 10-12 10:05 | +5 | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-12 10:05 | +5 | ETH | DOWN | 0.71 | 0.76 | 0.22 |
| 10-12 10:05 | +10 stop | XRP | DOWN | 0.66 | 0.79 | 1.02 |
| 10-12 10:04 | +5 | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 10-12 10:04 | +5 | ETH | DOWN | 0.64 | 0.69 | 0.18 |
| 10-12 10:04 | +5 | SOL | DOWN | 0.60 | 0.66 | 0.27 |
