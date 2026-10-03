# Range-Scalp Bot

*Updated Sat Oct 03 12:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 736 | 638 | 98 (1) | 3 | $-231.75 | -5.0% |
| **+10¢** | 561 | 453 | 108 (2) | 3 | $-170.11 | -4.8% |
| **+15¢** | 474 | 358 | 116 (3) | 5 | $-155.36 | -5.2% |
| **+20¢** | 413 | 291 | 122 (3) | 6 | $-157.34 | -6.0% |
| **+10¢ (15¢ stop)** | 944 | 943 | 1 (1) | 1 | $-509.95 | -8.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 12:18 | +10 stop | ZEC | DOWN | 0.57 | open |  |
| 10-03 12:18 | +10 | ZEC | DOWN | 0.57 | open |  |
| 10-03 12:18 | +5 | ZEC | DOWN | 0.57 | open |  |
| 10-03 12:18 | +10 stop | XRP | DOWN | 0.48 | 0.61 | 0.95 |
| 10-03 12:18 | +20 | XRP | DOWN | 0.48 | open |  |
| 10-03 12:18 | +15 | XRP | DOWN | 0.48 | open |  |
| 10-03 12:18 | +10 | XRP | DOWN | 0.49 | 0.61 | 0.85 |
| 10-03 12:18 | +5 | XRP | DOWN | 0.49 | 0.61 | 0.85 |
| 10-03 12:18 | +10 stop | DOGE | DOWN | 0.53 | 0.64 | 0.75 |
| 10-03 12:18 | +20 | DOGE | DOWN | 0.53 | open |  |
| 10-03 12:18 | +15 | DOGE | DOWN | 0.53 | open |  |
| 10-03 12:18 | +10 | DOGE | DOWN | 0.53 | 0.64 | 0.75 |
| 10-03 12:18 | +5 | DOGE | DOWN | 0.53 | 0.64 | 0.75 |
| 10-03 12:16 | +10 stop | BTC | UP | 0.66 | 0.80 | 1.12 |
| 10-03 12:16 | +20 | BTC | UP | 0.66 | 0.88 | 1.96 |
| 10-03 12:16 | +15 | BTC | UP | 0.66 | 0.88 | 1.96 |
| 10-03 12:16 | +10 | BTC | UP | 0.66 | 0.80 | 1.12 |
| 10-03 12:16 | +5 | BTC | UP | 0.66 | 0.72 | 0.29 |
| 10-03 12:16 | +5 | ETH | DOWN | 0.54 | open |  |
| 10-03 12:15 | +10 stop | ZEC | DOWN | 0.67 | 0.81 | 1.13 |
| 10-03 12:15 | +20 | ZEC | DOWN | 0.69 | open |  |
| 10-03 12:15 | +15 | ZEC | DOWN | 0.69 | open |  |
| 10-03 12:15 | +10 | ZEC | DOWN | 0.69 | 0.81 | 0.96 |
| 10-03 12:15 | +5 | ZEC | DOWN | 0.69 | 0.74 | 0.23 |
| 10-03 12:15 | +10 stop | SOL | DOWN | 0.66 | 0.51 | -1.84 |
| 10-03 12:15 | +20 | SOL | DOWN | 0.66 | open |  |
| 10-03 12:15 | +15 | SOL | DOWN | 0.66 | open |  |
| 10-03 12:15 | +10 | SOL | DOWN | 0.66 | open |  |
| 10-03 12:15 | +5 | SOL | DOWN | 0.66 | open |  |
| 10-03 12:15 | +10 stop | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-03 12:15 | +20 | HYPE | DOWN | 0.70 | open |  |
| 10-03 12:15 | +15 | HYPE | DOWN | 0.70 | 0.85 | 1.26 |
| 10-03 12:15 | +10 | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-03 12:15 | +5 | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-03 12:15 | +10 stop | ETH | DOWN | 0.61 | 0.25 | -3.91 |
| 10-03 12:15 | +20 | ETH | DOWN | 0.61 | open |  |
| 10-03 12:15 | +15 | ETH | DOWN | 0.61 | open |  |
| 10-03 12:15 | +10 | ETH | DOWN | 0.61 | open |  |
| 10-03 12:15 | +5 | ETH | DOWN | 0.61 | 0.67 | 0.27 |
| 10-03 12:09 | +10 stop | BTC | UP | 0.64 | 0.85 | 1.84 |
