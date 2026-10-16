# Range-Scalp Bot

*Updated Fri Oct 16 10:49 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19101 | 16604 | 2497 (28) | 5 | $-5718.60 | -4.8% |
| **+10¢** | 14395 | 11506 | 2889 (40) | 6 | $-5163.26 | -5.7% |
| **+15¢** | 12052 | 8946 | 3106 (59) | 6 | $-4639.65 | -6.1% |
| **+20¢** | 10694 | 7439 | 3255 (78) | 6 | $-4106.07 | -6.1% |
| **+10¢ (15¢ stop)** | 23488 | 23438 | 50 (29) | 5 | $-9049.05 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 10:48 | +10 stop | XRP | UP | 0.58 | 0.69 | 0.77 |
| 10-16 10:48 | +5 | SOL | DOWN | 0.70 | open |  |
| 10-16 10:48 | +10 stop | ZEC | DOWN | 0.69 | open |  |
| 10-16 10:48 | +20 | ZEC | DOWN | 0.69 | open |  |
| 10-16 10:48 | +15 | ZEC | DOWN | 0.69 | open |  |
| 10-16 10:48 | +10 | ZEC | DOWN | 0.69 | open |  |
| 10-16 10:48 | +5 | ZEC | DOWN | 0.69 | open |  |
| 10-16 10:47 | +5 | ETH | DOWN | 0.65 | open |  |
| 10-16 10:46 | +10 stop | BTC | DOWN | 0.68 | open |  |
| 10-16 10:46 | +20 | BTC | DOWN | 0.68 | open |  |
| 10-16 10:46 | +15 | BTC | DOWN | 0.68 | open |  |
| 10-16 10:46 | +10 | BTC | DOWN | 0.68 | open |  |
| 10-16 10:46 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 10-16 10:45 | +10 stop | SOL | DOWN | 0.68 | open |  |
| 10-16 10:45 | +20 | SOL | DOWN | 0.68 | open |  |
| 10-16 10:45 | +15 | SOL | DOWN | 0.68 | open |  |
| 10-16 10:45 | +10 | SOL | DOWN | 0.68 | open |  |
| 10-16 10:45 | +5 | SOL | DOWN | 0.68 | 0.73 | 0.20 |
| 10-16 10:45 | +10 stop | HYPE | DOWN | 0.64 | open |  |
| 10-16 10:45 | +20 | HYPE | DOWN | 0.64 | open |  |
| 10-16 10:45 | +15 | HYPE | DOWN | 0.64 | open |  |
| 10-16 10:45 | +10 | HYPE | DOWN | 0.64 | open |  |
| 10-16 10:45 | +5 | HYPE | DOWN | 0.64 | open |  |
| 10-16 10:45 | +10 stop | ETH | DOWN | 0.60 | open |  |
| 10-16 10:45 | +20 | ETH | DOWN | 0.60 | open |  |
| 10-16 10:45 | +15 | ETH | DOWN | 0.60 | open |  |
| 10-16 10:45 | +10 | ETH | DOWN | 0.60 | open |  |
| 10-16 10:45 | +5 | ETH | DOWN | 0.60 | 0.65 | 0.17 |
| 10-16 10:45 | +10 stop | XRP | DOWN | 0.58 | 0.40 | -2.15 |
| 10-16 10:45 | +20 | XRP | DOWN | 0.58 | open |  |
| 10-16 10:45 | +15 | XRP | DOWN | 0.58 | open |  |
| 10-16 10:45 | +10 | XRP | DOWN | 0.58 | open |  |
| 10-16 10:45 | +5 | XRP | DOWN | 0.58 | open |  |
| 10-16 10:31 | +10 stop | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 10-16 10:31 | +20 | NEAR | UP | 0.66 | 0.86 | 1.75 |
| 10-16 10:31 | +15 | NEAR | UP | 0.66 | 0.82 | 1.33 |
| 10-16 10:31 | +10 | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 10-16 10:31 | +5 | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 10-16 10:31 | +10 stop | ZEC | UP | 0.70 | 0.86 | 1.36 |
| 10-16 10:31 | +20 | ZEC | UP | 0.70 | 0.92 | 1.99 |
