# Range-Scalp Bot

*Updated Tue Oct 06 17:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5260 | 4557 | 703 (7) | 5 | $-1637.49 | -4.9% |
| **+10¢** | 4018 | 3199 | 819 (12) | 7 | $-1504.63 | -6.0% |
| **+15¢** | 3365 | 2497 | 868 (15) | 8 | $-1311.46 | -6.2% |
| **+20¢** | 3012 | 2110 | 902 (22) | 8 | $-1038.05 | -5.5% |
| **+10¢ (15¢ stop)** | 6433 | 6418 | 15 (9) | 1 | $-2356.33 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 17:37 | +10 stop | NEAR | UP | 0.56 | open |  |
| 10-06 17:36 | +10 stop | NEAR | UP | 0.52 | 0.64 | 0.86 |
| 10-06 17:36 | +10 stop | XRP | UP | 0.59 | 0.71 | 0.88 |
| 10-06 17:35 | +10 stop | ZEC | UP | 0.59 | 0.73 | 1.10 |
| 10-06 17:35 | +5 | ZEC | UP | 0.59 | 0.73 | 1.10 |
| 10-06 17:35 | +10 stop | BTC | DOWN | 0.58 | 0.75 | 1.38 |
| 10-06 17:35 | +10 stop | NEAR | DOWN | 0.64 | 0.45 | -2.22 |
| 10-06 17:35 | +20 | NEAR | DOWN | 0.64 | open |  |
| 10-06 17:35 | +15 | NEAR | DOWN | 0.64 | open |  |
| 10-06 17:35 | +10 | NEAR | DOWN | 0.64 | open |  |
| 10-06 17:35 | +5 | NEAR | DOWN | 0.64 | open |  |
| 10-06 17:35 | +10 stop | SOL | UP | 0.59 | 0.71 | 0.88 |
| 10-06 17:35 | +10 stop | HYPE | UP | 0.69 | 0.83 | 1.11 |
| 10-06 17:35 | +5 | HYPE | UP | 0.69 | 0.79 | 0.69 |
| 10-06 17:34 | +10 stop | ETH | DOWN | 0.57 | 0.33 | -2.74 |
| 10-06 17:34 | +20 | ETH | DOWN | 0.57 | open |  |
| 10-06 17:34 | +15 | ETH | DOWN | 0.57 | open |  |
| 10-06 17:34 | +10 | ETH | DOWN | 0.57 | open |  |
| 10-06 17:34 | +5 | ETH | DOWN | 0.57 | open |  |
| 10-06 17:34 | +10 stop | XRP | DOWN | 0.65 | 0.37 | -3.13 |
| 10-06 17:34 | +20 | XRP | DOWN | 0.65 | open |  |
| 10-06 17:34 | +15 | XRP | DOWN | 0.65 | open |  |
| 10-06 17:34 | +10 | XRP | DOWN | 0.65 | open |  |
| 10-06 17:34 | +5 | XRP | DOWN | 0.65 | open |  |
| 10-06 17:32 | +10 stop | ZEC | DOWN | 0.71 | 0.53 | -2.13 |
| 10-06 17:32 | +20 | ZEC | DOWN | 0.71 | open |  |
| 10-06 17:32 | +15 | ZEC | DOWN | 0.71 | open |  |
| 10-06 17:32 | +10 | ZEC | DOWN | 0.71 | open |  |
| 10-06 17:32 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-06 17:32 | +10 stop | BTC | DOWN | 0.66 | 0.48 | -2.14 |
| 10-06 17:32 | +20 | BTC | DOWN | 0.66 | open |  |
| 10-06 17:32 | +15 | BTC | DOWN | 0.66 | open |  |
| 10-06 17:32 | +10 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-06 17:32 | +5 | BTC | DOWN | 0.66 | 0.75 | 0.60 |
| 10-06 17:31 | +10 stop | BNB | DOWN | 0.67 | 0.48 | -2.24 |
| 10-06 17:31 | +20 | BNB | DOWN | 0.67 | open |  |
| 10-06 17:31 | +15 | BNB | DOWN | 0.67 | open |  |
| 10-06 17:31 | +10 | BNB | DOWN | 0.67 | open |  |
| 10-06 17:31 | +5 | BNB | DOWN | 0.67 | open |  |
| 10-06 17:31 | +10 stop | HYPE | DOWN | 0.67 | 0.51 | -1.94 |
