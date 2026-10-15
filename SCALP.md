# Range-Scalp Bot

*Updated Thu Oct 15 12:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17509 | 15204 | 2305 (28) | 0 | $-5303.02 | -4.8% |
| **+10¢** | 13233 | 10564 | 2669 (40) | 0 | $-4798.01 | -5.8% |
| **+15¢** | 11107 | 8237 | 2870 (59) | 2 | $-4285.24 | -6.1% |
| **+20¢** | 9866 | 6860 | 3006 (77) | 6 | $-3748.81 | -6.1% |
| **+10¢ (15¢ stop)** | 21540 | 21490 | 50 (29) | 0 | $-8307.05 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 12:33 | +10 stop | ZEC | DOWN | 0.43 | 0.57 | 1.04 |
| 10-15 12:33 | +15 | ZEC | DOWN | 0.40 | 0.57 | 1.35 |
| 10-15 12:33 | +10 | ZEC | DOWN | 0.40 | 0.57 | 1.35 |
| 10-15 12:33 | +5 | ZEC | DOWN | 0.40 | 0.57 | 1.35 |
| 10-15 12:31 | +10 stop | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-15 12:31 | +20 | HYPE | DOWN | 0.68 | open |  |
| 10-15 12:31 | +15 | HYPE | DOWN | 0.68 | 0.83 | 1.24 |
| 10-15 12:31 | +10 | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-15 12:31 | +5 | HYPE | DOWN | 0.68 | 0.75 | 0.40 |
| 10-15 12:31 | +10 stop | XRP | DOWN | 0.66 | 0.85 | 1.65 |
| 10-15 12:31 | +20 | XRP | DOWN | 0.67 | open |  |
| 10-15 12:31 | +15 | XRP | DOWN | 0.67 | 0.85 | 1.55 |
| 10-15 12:31 | +10 | XRP | DOWN | 0.67 | 0.85 | 1.55 |
| 10-15 12:31 | +5 | XRP | DOWN | 0.67 | 0.73 | 0.30 |
| 10-15 12:31 | +10 stop | DOGE | DOWN | 0.70 | 0.89 | 1.68 |
| 10-15 12:31 | +20 | DOGE | DOWN | 0.70 | open |  |
| 10-15 12:31 | +15 | DOGE | DOWN | 0.70 | 0.89 | 1.68 |
| 10-15 12:31 | +10 | DOGE | DOWN | 0.70 | 0.89 | 1.68 |
| 10-15 12:31 | +5 | DOGE | DOWN | 0.70 | 0.75 | 0.21 |
| 10-15 12:31 | +10 stop | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 10-15 12:31 | +20 | SOL | DOWN | 0.65 | open |  |
| 10-15 12:31 | +15 | SOL | DOWN | 0.65 | open |  |
| 10-15 12:31 | +10 | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 10-15 12:31 | +5 | SOL | DOWN | 0.65 | 0.71 | 0.29 |
| 10-15 12:31 | +10 stop | ZEC | DOWN | 0.67 | 0.82 | 1.23 |
| 10-15 12:31 | +20 | ZEC | DOWN | 0.67 | open |  |
| 10-15 12:31 | +15 | ZEC | DOWN | 0.67 | 0.82 | 1.23 |
| 10-15 12:31 | +10 | ZEC | DOWN | 0.67 | 0.82 | 1.23 |
| 10-15 12:31 | +5 | ZEC | DOWN | 0.66 | 0.82 | 1.30 |
| 10-15 12:31 | +10 stop | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 10-15 12:31 | +20 | NEAR | DOWN | 0.63 | open |  |
| 10-15 12:31 | +15 | NEAR | DOWN | 0.63 | open |  |
| 10-15 12:31 | +10 | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 10-15 12:31 | +5 | NEAR | DOWN | 0.63 | 0.70 | 0.38 |
| 10-15 12:28 | +10 stop | SOL | DOWN | 0.49 | 0.63 | 1.05 |
| 10-15 12:27 | +10 stop | BNB | DOWN | 0.39 | 0.57 | 1.41 |
| 10-15 12:27 | +20 | BNB | DOWN | 0.39 | yes | -4.11 |
| 10-15 12:27 | +15 | BNB | DOWN | 0.39 | 0.57 | 1.41 |
| 10-15 12:27 | +10 | BNB | DOWN | 0.39 | 0.57 | 1.41 |
| 10-15 12:27 | +5 | BNB | DOWN | 0.39 | 0.57 | 1.41 |
