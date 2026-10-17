# Range-Scalp Bot

*Updated Sat Oct 17 12:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20932 | 18214 | 2718 (29) | 2 | $-6126.39 | -4.6% |
| **+10¢** | 15755 | 12621 | 3134 (41) | 2 | $-5445.23 | -5.5% |
| **+15¢** | 13169 | 9795 | 3374 (61) | 3 | $-4931.90 | -6.0% |
| **+20¢** | 11676 | 8144 | 3532 (80) | 3 | $-4346.94 | -5.9% |
| **+10¢ (15¢ stop)** | 25724 | 25674 | 50 (29) | 0 | $-9794.91 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 12:12 | +10 stop | BTC | UP | 0.65 | 0.34 | -3.42 |
| 10-17 12:12 | +20 | BTC | UP | 0.65 | open |  |
| 10-17 12:12 | +15 | BTC | UP | 0.65 | open |  |
| 10-17 12:12 | +10 | BTC | UP | 0.65 | open |  |
| 10-17 12:12 | +5 | BTC | UP | 0.64 | open |  |
| 10-17 12:11 | +10 stop | ETH | UP | 0.41 | 0.57 | 1.25 |
| 10-17 12:11 | +10 | ETH | UP | 0.42 | 0.57 | 1.14 |
| 10-17 12:11 | +5 | ETH | UP | 0.42 | 0.57 | 1.14 |
| 10-17 12:08 | +10 stop | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 10-17 12:07 | +10 stop | HYPE | DOWN | 0.67 | 0.82 | 1.23 |
| 10-17 12:07 | +20 | HYPE | DOWN | 0.68 | 0.88 | 1.76 |
| 10-17 12:07 | +15 | HYPE | DOWN | 0.68 | 0.87 | 1.66 |
| 10-17 12:07 | +10 | HYPE | DOWN | 0.68 | 0.82 | 1.13 |
| 10-17 12:07 | +5 | HYPE | DOWN | 0.68 | 0.75 | 0.40 |
| 10-17 12:06 | +10 stop | ETH | DOWN | 0.65 | 0.83 | 1.54 |
| 10-17 12:05 | +10 stop | HYPE | UP | 0.46 | 0.57 | 0.70 |
| 10-17 12:04 | +10 stop | ETH | UP | 0.56 | 0.34 | -2.54 |
| 10-17 12:04 | +10 stop | HYPE | DOWN | 0.57 | 0.35 | -2.54 |
| 10-17 12:04 | +20 | HYPE | DOWN | 0.57 | 0.80 | 2.00 |
| 10-17 12:04 | +15 | HYPE | DOWN | 0.57 | 0.80 | 2.00 |
| 10-17 12:04 | +10 | HYPE | DOWN | 0.57 | 0.80 | 2.00 |
| 10-17 12:04 | +5 | HYPE | DOWN | 0.57 | 0.63 | 0.25 |
| 10-17 12:04 | +10 stop | BNB | DOWN | 0.55 | 0.70 | 1.17 |
| 10-17 12:03 | +10 stop | ETH | DOWN | 0.59 | 0.44 | -1.85 |
| 10-17 12:02 | +10 stop | BNB | DOWN | 0.58 | 0.76 | 1.49 |
| 10-17 12:01 | +10 stop | ETH | UP | 0.63 | 0.41 | -2.54 |
| 10-17 12:01 | +20 | ETH | UP | 0.63 | open |  |
| 10-17 12:01 | +15 | ETH | UP | 0.63 | open |  |
| 10-17 12:01 | +10 | ETH | UP | 0.63 | 0.73 | 0.69 |
| 10-17 12:01 | +5 | ETH | UP | 0.63 | 0.73 | 0.69 |
| 10-17 12:01 | +10 stop | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-17 12:01 | +20 | HYPE | DOWN | 0.62 | 0.82 | 1.72 |
| 10-17 12:01 | +15 | HYPE | DOWN | 0.62 | 0.80 | 1.51 |
| 10-17 12:01 | +10 | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-17 12:01 | +5 | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-17 12:01 | +10 stop | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 10-17 12:01 | +20 | SOL | DOWN | 0.63 | 0.83 | 1.73 |
| 10-17 12:01 | +15 | SOL | DOWN | 0.62 | 0.80 | 1.51 |
| 10-17 12:01 | +10 | SOL | DOWN | 0.62 | 0.75 | 0.99 |
| 10-17 12:01 | +5 | SOL | DOWN | 0.62 | 0.75 | 0.99 |
