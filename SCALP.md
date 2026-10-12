# Range-Scalp Bot

*Updated Mon Oct 12 11:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13485 | 11668 | 1817 (25) | 0 | $-4287.41 | -5.0% |
| **+10¢** | 10211 | 8106 | 2105 (37) | 1 | $-3985.81 | -6.2% |
| **+15¢** | 8595 | 6344 | 2251 (55) | 1 | $-3498.03 | -6.5% |
| **+20¢** | 7650 | 5300 | 2350 (70) | 1 | $-2987.62 | -6.2% |
| **+10¢ (15¢ stop)** | 16580 | 16539 | 41 (25) | 1 | $-6476.61 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 11:08 | +10 stop | ZEC | DOWN | 0.57 | open |  |
| 10-12 11:08 | +20 | ZEC | DOWN | 0.56 | open |  |
| 10-12 11:08 | +15 | ZEC | DOWN | 0.55 | open |  |
| 10-12 11:08 | +10 | ZEC | DOWN | 0.55 | open |  |
| 10-12 11:08 | +5 | ZEC | DOWN | 0.55 | 0.64 | 0.55 |
| 10-12 11:03 | +5 | ZEC | DOWN | 0.61 | 0.68 | 0.38 |
| 10-12 11:02 | +10 stop | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-12 11:02 | +20 | ZEC | DOWN | 0.58 | 0.82 | 2.11 |
| 10-12 11:02 | +15 | ZEC | DOWN | 0.58 | 0.82 | 2.11 |
| 10-12 11:02 | +10 | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-12 11:02 | +5 | ZEC | DOWN | 0.58 | 0.64 | 0.25 |
| 10-12 11:01 | +10 stop | ETH | DOWN | 0.70 | 0.81 | 0.84 |
| 10-12 11:01 | +20 | ETH | DOWN | 0.70 | 0.91 | 1.90 |
| 10-12 11:01 | +15 | ETH | DOWN | 0.70 | 0.86 | 1.36 |
| 10-12 11:01 | +10 | ETH | DOWN | 0.70 | 0.81 | 0.84 |
| 10-12 11:01 | +5 | ETH | DOWN | 0.70 | 0.78 | 0.52 |
| 10-12 11:01 | +10 stop | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-12 11:01 | +20 | BTC | DOWN | 0.70 | 0.92 | 1.98 |
| 10-12 11:01 | +15 | BTC | DOWN | 0.70 | 0.86 | 1.36 |
| 10-12 11:01 | +10 | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-12 11:01 | +5 | BTC | DOWN | 0.70 | 0.79 | 0.63 |
| 10-12 11:01 | +10 stop | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 10-12 11:01 | +20 | DOGE | DOWN | 0.69 | 0.90 | 1.88 |
| 10-12 11:01 | +15 | DOGE | DOWN | 0.69 | 0.84 | 1.25 |
| 10-12 11:01 | +10 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 10-12 11:01 | +5 | DOGE | DOWN | 0.70 | 0.75 | 0.21 |
| 10-12 11:01 | +10 stop | XRP | DOWN | 0.59 | 0.73 | 1.09 |
| 10-12 11:01 | +20 | XRP | DOWN | 0.59 | 0.80 | 1.81 |
| 10-12 11:01 | +15 | XRP | DOWN | 0.59 | 0.80 | 1.81 |
| 10-12 11:01 | +10 | XRP | DOWN | 0.59 | 0.73 | 1.09 |
| 10-12 11:01 | +5 | XRP | DOWN | 0.59 | 0.67 | 0.47 |
| 10-12 11:00 | +10 stop | NEAR | DOWN | 0.61 | 0.78 | 1.41 |
| 10-12 11:00 | +20 | NEAR | DOWN | 0.61 | 0.86 | 2.25 |
| 10-12 11:00 | +15 | NEAR | DOWN | 0.61 | 0.78 | 1.41 |
| 10-12 11:00 | +10 | NEAR | DOWN | 0.61 | 0.78 | 1.41 |
| 10-12 11:00 | +5 | NEAR | DOWN | 0.62 | 0.67 | 0.19 |
| 10-12 11:00 | +10 stop | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-12 11:00 | +20 | SOL | DOWN | 0.63 | 0.85 | 1.94 |
| 10-12 11:00 | +15 | SOL | DOWN | 0.63 | 0.82 | 1.62 |
| 10-12 11:00 | +10 | SOL | DOWN | 0.64 | 0.74 | 0.69 |
