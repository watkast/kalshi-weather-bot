# Range-Scalp Bot

*Updated Tue Oct 06 00:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4371 | 3768 | 603 (6) | 4 | $-1479.60 | -5.4% |
| **+10¢** | 3365 | 2667 | 698 (9) | 6 | $-1350.63 | -6.4% |
| **+15¢** | 2823 | 2086 | 737 (12) | 6 | $-1169.35 | -6.6% |
| **+20¢** | 2526 | 1757 | 769 (17) | 6 | $-996.77 | -6.3% |
| **+10¢ (15¢ stop)** | 5355 | 5344 | 11 (6) | 5 | $-1899.52 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 00:05 | +5 | ETH | UP | 0.62 | open |  |
| 10-06 00:05 | +10 stop | HYPE | UP | 0.55 | open |  |
| 10-06 00:05 | +10 stop | ETH | UP | 0.58 | open |  |
| 10-06 00:05 | +10 stop | NEAR | DOWN | 0.60 | open |  |
| 10-06 00:05 | +10 stop | SOL | UP | 0.64 | open |  |
| 10-06 00:05 | +20 | SOL | UP | 0.64 | open |  |
| 10-06 00:05 | +15 | SOL | UP | 0.64 | open |  |
| 10-06 00:05 | +10 | SOL | UP | 0.64 | open |  |
| 10-06 00:05 | +5 | SOL | UP | 0.64 | 0.69 | 0.18 |
| 10-06 00:04 | +10 stop | BTC | UP | 0.56 | open |  |
| 10-06 00:04 | +15 | BTC | UP | 0.56 | open |  |
| 10-06 00:04 | +10 | BTC | UP | 0.56 | open |  |
| 10-06 00:04 | +5 | BTC | UP | 0.56 | open |  |
| 10-06 00:04 | +5 | ETH | UP | 0.57 | 0.63 | 0.25 |
| 10-06 00:04 | +5 | HYPE | UP | 0.62 | open |  |
| 10-06 00:04 | +10 stop | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 10-06 00:03 | +10 stop | HYPE | UP | 0.70 | 0.53 | -2.03 |
| 10-06 00:03 | +20 | HYPE | UP | 0.69 | open |  |
| 10-06 00:03 | +15 | HYPE | UP | 0.69 | open |  |
| 10-06 00:03 | +10 | HYPE | UP | 0.69 | open |  |
| 10-06 00:03 | +5 | HYPE | UP | 0.69 | 0.76 | 0.42 |
| 10-06 00:02 | +10 stop | NEAR | UP | 0.65 | 0.45 | -2.35 |
| 10-06 00:02 | +10 stop | ETH | UP | 0.71 | 0.56 | -1.83 |
| 10-06 00:02 | +20 | ETH | UP | 0.71 | open |  |
| 10-06 00:02 | +15 | ETH | UP | 0.71 | open |  |
| 10-06 00:02 | +10 | ETH | UP | 0.71 | open |  |
| 10-06 00:02 | +5 | ETH | UP | 0.71 | 0.77 | 0.32 |
| 10-06 00:02 | +10 stop | DOGE | DOWN | 0.58 | 0.74 | 1.28 |
| 10-06 00:02 | +10 | DOGE | DOWN | 0.58 | 0.74 | 1.28 |
| 10-06 00:02 | +10 stop | ZEC | DOWN | 0.64 | 0.48 | -1.95 |
| 10-06 00:02 | +20 | ZEC | DOWN | 0.64 | 0.86 | 1.94 |
| 10-06 00:02 | +15 | ZEC | DOWN | 0.64 | 0.86 | 1.94 |
| 10-06 00:02 | +10 | ZEC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-06 00:02 | +5 | ZEC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-06 00:01 | +10 stop | BTC | UP | 0.59 | 0.69 | 0.68 |
| 10-06 00:01 | +20 | BTC | UP | 0.59 | open |  |
| 10-06 00:01 | +15 | BTC | UP | 0.59 | 0.77 | 1.50 |
| 10-06 00:01 | +10 | BTC | UP | 0.59 | 0.69 | 0.68 |
| 10-06 00:01 | +5 | BTC | UP | 0.59 | 0.69 | 0.68 |
| 10-06 00:01 | +10 stop | NEAR | DOWN | 0.64 | 0.45 | -2.24 |
