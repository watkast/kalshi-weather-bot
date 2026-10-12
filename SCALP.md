# Range-Scalp Bot

*Updated Mon Oct 12 00:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12712 | 10975 | 1737 (25) | 5 | $-4182.47 | -5.2% |
| **+10¢** | 9642 | 7634 | 2008 (37) | 6 | $-3892.21 | -6.4% |
| **+15¢** | 8113 | 5974 | 2139 (55) | 6 | $-3377.70 | -6.6% |
| **+20¢** | 7229 | 4999 | 2230 (69) | 6 | $-2878.25 | -6.3% |
| **+10¢ (15¢ stop)** | 15670 | 15629 | 41 (25) | 4 | $-6125.49 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 00:07 | +5 | ETH | DOWN | 0.63 | open |  |
| 10-12 00:07 | +10 stop | SOL | DOWN | 0.65 | open |  |
| 10-12 00:06 | +10 stop | BNB | UP | 0.69 | open |  |
| 10-12 00:06 | +20 | BNB | UP | 0.69 | open |  |
| 10-12 00:06 | +15 | BNB | UP | 0.69 | open |  |
| 10-12 00:06 | +10 | BNB | UP | 0.69 | open |  |
| 10-12 00:06 | +5 | BNB | UP | 0.69 | open |  |
| 10-12 00:06 | +10 | ETH | DOWN | 0.64 | open |  |
| 10-12 00:06 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.17 |
| 10-12 00:06 | +10 stop | ETH | DOWN | 0.64 | open |  |
| 10-12 00:06 | +10 stop | ETH | UP | 0.35 | 0.57 | 1.86 |
| 10-12 00:06 | +15 | DOGE | UP | 0.56 | open |  |
| 10-12 00:05 | +10 stop | SOL | DOWN | 0.62 | 0.76 | 1.10 |
| 10-12 00:05 | +10 stop | BTC | DOWN | 0.57 | 0.79 | 1.90 |
| 10-12 00:05 | +20 | BTC | DOWN | 0.57 | 0.79 | 1.90 |
| 10-12 00:05 | +15 | BTC | DOWN | 0.57 | 0.79 | 1.90 |
| 10-12 00:05 | +10 | BTC | DOWN | 0.57 | 0.79 | 1.90 |
| 10-12 00:05 | +5 | BTC | DOWN | 0.57 | 0.79 | 1.90 |
| 10-12 00:04 | +10 stop | ZEC | UP | 0.70 | 0.50 | -2.33 |
| 10-12 00:04 | +10 stop | DOGE | UP | 0.68 | open |  |
| 10-12 00:04 | +10 | DOGE | UP | 0.68 | open |  |
| 10-12 00:04 | +5 | DOGE | UP | 0.68 | open |  |
| 10-12 00:04 | +10 stop | ETH | UP | 0.62 | 0.46 | -1.95 |
| 10-12 00:03 | +5 | DOGE | UP | 0.60 | 0.66 | 0.27 |
| 10-12 00:03 | +5 | SOL | UP | 0.63 | open |  |
| 10-12 00:03 | +10 stop | XRP | UP | 0.61 | 0.71 | 0.68 |
| 10-12 00:03 | +20 | XRP | UP | 0.61 | open |  |
| 10-12 00:03 | +15 | XRP | UP | 0.62 | open |  |
| 10-12 00:03 | +10 | XRP | UP | 0.62 | open |  |
| 10-12 00:03 | +5 | XRP | UP | 0.62 | 0.71 | 0.58 |
| 10-12 00:02 | +10 stop | DOGE | UP | 0.55 | 0.66 | 0.76 |
| 10-12 00:02 | +20 | DOGE | UP | 0.55 | open |  |
| 10-12 00:02 | +15 | DOGE | UP | 0.55 | 0.71 | 1.27 |
| 10-12 00:02 | +10 | DOGE | UP | 0.55 | 0.66 | 0.76 |
| 10-12 00:02 | +5 | DOGE | UP | 0.55 | 0.60 | 0.15 |
| 10-12 00:02 | +10 stop | SOL | UP | 0.58 | 0.41 | -2.05 |
| 10-12 00:02 | +20 | SOL | UP | 0.58 | open |  |
| 10-12 00:02 | +15 | SOL | UP | 0.58 | open |  |
| 10-12 00:02 | +10 | SOL | UP | 0.58 | open |  |
| 10-12 00:02 | +5 | SOL | UP | 0.58 | 0.66 | 0.46 |
