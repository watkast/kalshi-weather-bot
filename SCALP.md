# Range-Scalp Bot

*Updated Mon Oct 26 10:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34649 | 30250 | 4399 (43) | 0 | $-9601.56 | -4.4% |
| **+10¢** | 25932 | 20845 | 5087 (65) | 3 | $-8415.39 | -5.2% |
| **+15¢** | 21694 | 16217 | 5477 (89) | 2 | $-7530.36 | -5.5% |
| **+20¢** | 19225 | 13482 | 5743 (112) | 5 | $-6650.15 | -5.5% |
| **+10¢ (15¢ stop)** | 42429 | 42367 | 62 (33) | 4 | $-16131.48 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 10:07 | +5 | NEAR | DOWN | 0.65 | 0.70 | 0.19 |
| 10-26 10:06 | +10 stop | DOGE | DOWN | 0.68 | open |  |
| 10-26 10:06 | +5 | SOL | DOWN | 0.61 | 0.67 | 0.27 |
| 10-26 10:06 | +10 stop | ZEC | DOWN | 0.63 | 0.80 | 1.41 |
| 10-26 10:06 | +20 | ZEC | DOWN | 0.65 | open |  |
| 10-26 10:06 | +15 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-26 10:06 | +10 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-26 10:06 | +5 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-26 10:06 | +10 | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 10-26 10:06 | +5 | NEAR | DOWN | 0.62 | 0.68 | 0.27 |
| 10-26 10:05 | +10 | BNB | DOWN | 0.71 | open |  |
| 10-26 10:05 | +5 | BNB | DOWN | 0.71 | 0.76 | 0.25 |
| 10-26 10:05 | +10 stop | BNB | DOWN | 0.70 | open |  |
| 10-26 10:04 | +10 stop | NEAR | DOWN | 0.63 | open |  |
| 10-26 10:04 | +20 | NEAR | DOWN | 0.63 | open |  |
| 10-26 10:04 | +15 | NEAR | DOWN | 0.60 | open |  |
| 10-26 10:04 | +10 | NEAR | DOWN | 0.60 | 0.71 | 0.78 |
| 10-26 10:04 | +5 | NEAR | DOWN | 0.60 | 0.67 | 0.37 |
| 10-26 10:04 | +5 | BNB | DOWN | 0.63 | 0.68 | 0.17 |
| 10-26 10:03 | +10 stop | DOGE | DOWN | 0.67 | 0.52 | -1.84 |
| 10-26 10:03 | +10 | DOGE | DOWN | 0.67 | open |  |
| 10-26 10:03 | +5 | DOGE | DOWN | 0.67 | 0.74 | 0.40 |
| 10-26 10:03 | +10 stop | SOL | DOWN | 0.67 | 0.83 | 1.34 |
| 10-26 10:03 | +20 | SOL | DOWN | 0.67 | open |  |
| 10-26 10:03 | +15 | SOL | DOWN | 0.67 | 0.83 | 1.34 |
| 10-26 10:03 | +10 | SOL | DOWN | 0.67 | 0.83 | 1.34 |
| 10-26 10:03 | +5 | SOL | DOWN | 0.67 | 0.73 | 0.30 |
| 10-26 10:03 | +5 | BNB | DOWN | 0.56 | 0.64 | 0.45 |
| 10-26 10:02 | +10 stop | HYPE | DOWN | 0.70 | open |  |
| 10-26 10:02 | +10 | HYPE | DOWN | 0.70 | open |  |
| 10-26 10:02 | +5 | HYPE | DOWN | 0.70 | 0.75 | 0.21 |
| 10-26 10:02 | +10 stop | BNB | DOWN | 0.55 | 0.68 | 0.96 |
| 10-26 10:02 | +20 | BNB | DOWN | 0.55 | 0.76 | 1.79 |
| 10-26 10:02 | +15 | BNB | DOWN | 0.55 | 0.70 | 1.17 |
| 10-26 10:02 | +10 | BNB | DOWN | 0.55 | 0.68 | 0.96 |
| 10-26 10:02 | +5 | BNB | DOWN | 0.55 | 0.61 | 0.25 |
| 10-26 10:01 | +10 stop | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-26 10:01 | +20 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-26 10:01 | +15 | BTC | DOWN | 0.69 | 0.85 | 1.36 |
| 10-26 10:01 | +10 | BTC | DOWN | 0.69 | 0.80 | 0.84 |
