# Range-Scalp Bot

*Updated Wed Oct 14 22:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16615 | 14404 | 2211 (28) | 1 | $-5190.75 | -5.0% |
| **+10¢** | 12569 | 10007 | 2562 (40) | 3 | $-4741.23 | -6.0% |
| **+15¢** | 10560 | 7808 | 2752 (59) | 4 | $-4257.86 | -6.4% |
| **+20¢** | 9381 | 6497 | 2884 (76) | 6 | $-3766.60 | -6.4% |
| **+10¢ (15¢ stop)** | 20454 | 20404 | 50 (29) | 4 | $-7870.89 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 22:17 | +10 stop | ZEC | DOWN | 0.62 | open |  |
| 10-14 22:17 | +10 | ZEC | DOWN | 0.62 | open |  |
| 10-14 22:17 | +5 | ZEC | DOWN | 0.62 | open |  |
| 10-14 22:16 | +10 stop | XRP | DOWN | 0.65 | open |  |
| 10-14 22:16 | +20 | XRP | DOWN | 0.65 | open |  |
| 10-14 22:16 | +15 | XRP | DOWN | 0.65 | open |  |
| 10-14 22:16 | +10 | XRP | DOWN | 0.65 | open |  |
| 10-14 22:16 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 10-14 22:16 | +10 stop | DOGE | DOWN | 0.71 | open |  |
| 10-14 22:16 | +10 stop | ETH | DOWN | 0.68 | 0.81 | 1.03 |
| 10-14 22:16 | +20 | ETH | DOWN | 0.68 | open |  |
| 10-14 22:16 | +15 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 10-14 22:16 | +10 | ETH | DOWN | 0.68 | 0.81 | 1.03 |
| 10-14 22:16 | +5 | ETH | DOWN | 0.68 | 0.75 | 0.40 |
| 10-14 22:16 | +10 stop | NEAR | DOWN | 0.70 | open |  |
| 10-14 22:16 | +20 | NEAR | DOWN | 0.70 | open |  |
| 10-14 22:16 | +15 | NEAR | DOWN | 0.70 | open |  |
| 10-14 22:16 | +10 | NEAR | DOWN | 0.70 | open |  |
| 10-14 22:16 | +5 | NEAR | DOWN | 0.70 | 0.77 | 0.42 |
| 10-14 22:16 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-14 22:16 | +20 | BTC | DOWN | 0.67 | open |  |
| 10-14 22:16 | +15 | BTC | DOWN | 0.67 | open |  |
| 10-14 22:16 | +10 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-14 22:16 | +5 | BTC | DOWN | 0.67 | 0.73 | 0.30 |
| 10-14 22:16 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.79 |
| 10-14 22:16 | +20 | ZEC | DOWN | 0.65 | open |  |
| 10-14 22:16 | +15 | ZEC | DOWN | 0.65 | open |  |
| 10-14 22:16 | +10 | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-14 22:16 | +5 | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-14 22:16 | +10 stop | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 10-14 22:16 | +20 | BNB | DOWN | 0.64 | open |  |
| 10-14 22:16 | +15 | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 10-14 22:16 | +10 | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 10-14 22:16 | +5 | BNB | DOWN | 0.64 | 0.70 | 0.28 |
| 10-14 22:08 | +5 | NEAR | DOWN | 0.65 | 0.79 | 1.12 |
| 10-14 22:07 | +10 stop | NEAR | DOWN | 0.55 | 0.79 | 2.10 |
| 10-14 22:07 | +10 | NEAR | DOWN | 0.55 | 0.79 | 2.10 |
| 10-14 22:07 | +5 | NEAR | DOWN | 0.55 | 0.62 | 0.35 |
| 10-14 22:05 | +10 stop | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 10-14 22:05 | +10 stop | NEAR | UP | 0.43 | 0.57 | 1.04 |
