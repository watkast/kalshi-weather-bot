# Range-Scalp Bot

*Updated Thu Oct 22 02:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28078 | 24464 | 3614 (39) | 5 | $-8082.21 | -4.6% |
| **+10¢** | 21093 | 16917 | 4176 (55) | 7 | $-7133.12 | -5.4% |
| **+15¢** | 17668 | 13176 | 4492 (78) | 8 | $-6350.25 | -5.7% |
| **+20¢** | 15636 | 10928 | 4708 (98) | 9 | $-5694.46 | -5.8% |
| **+10¢ (15¢ stop)** | 34475 | 34416 | 59 (32) | 5 | $-12892.92 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 02:04 | +5 | BNB | DOWN | 0.57 | 0.68 | 0.76 |
| 10-22 02:04 | +10 stop | NEAR | DOWN | 0.54 | open |  |
| 10-22 02:04 | +10 | XRP | DOWN | 0.71 | open |  |
| 10-22 02:04 | +5 | XRP | DOWN | 0.71 | open |  |
| 10-22 02:03 | +10 stop | XRP | DOWN | 0.61 | 0.74 | 0.99 |
| 10-22 02:03 | +5 | XRP | DOWN | 0.61 | 0.68 | 0.37 |
| 10-22 02:03 | +10 stop | ZEC | DOWN | 0.63 | open |  |
| 10-22 02:03 | +10 | ZEC | DOWN | 0.63 | open |  |
| 10-22 02:03 | +5 | ZEC | DOWN | 0.63 | open |  |
| 10-22 02:02 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-22 02:02 | +20 | SOL | DOWN | 0.64 | open |  |
| 10-22 02:02 | +15 | SOL | DOWN | 0.65 | open |  |
| 10-22 02:02 | +10 | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 10-22 02:02 | +5 | SOL | DOWN | 0.65 | 0.70 | 0.19 |
| 10-22 02:02 | +10 stop | ETH | DOWN | 0.66 | open |  |
| 10-22 02:02 | +20 | ETH | DOWN | 0.66 | open |  |
| 10-22 02:02 | +15 | ETH | DOWN | 0.66 | open |  |
| 10-22 02:02 | +10 | ETH | DOWN | 0.66 | open |  |
| 10-22 02:02 | +5 | ETH | DOWN | 0.66 | 0.75 | 0.60 |
| 10-22 02:02 | +10 stop | BTC | DOWN | 0.68 | open |  |
| 10-22 02:02 | +10 stop | BNB | UP | 0.56 | 0.31 | -2.83 |
| 10-22 02:02 | +20 | BNB | UP | 0.56 | open |  |
| 10-22 02:02 | +15 | BNB | UP | 0.56 | open |  |
| 10-22 02:02 | +10 | BNB | UP | 0.56 | open |  |
| 10-22 02:02 | +5 | BNB | UP | 0.56 | 0.64 | 0.45 |
| 10-22 02:02 | +10 stop | NEAR | UP | 0.62 | 0.46 | -1.95 |
| 10-22 02:02 | +20 | NEAR | UP | 0.62 | open |  |
| 10-22 02:02 | +15 | NEAR | UP | 0.62 | open |  |
| 10-22 02:02 | +10 | NEAR | UP | 0.62 | open |  |
| 10-22 02:02 | +5 | NEAR | UP | 0.62 | open |  |
| 10-22 02:01 | +10 stop | HYPE | UP | 0.57 | open |  |
| 10-22 02:01 | +20 | HYPE | UP | 0.57 | open |  |
| 10-22 02:01 | +15 | HYPE | UP | 0.58 | open |  |
| 10-22 02:01 | +10 | HYPE | UP | 0.58 | open |  |
| 10-22 02:01 | +5 | HYPE | UP | 0.58 | open |  |
| 10-22 02:01 | +5 | DOGE | DOWN | 0.61 | 0.69 | 0.48 |
| 10-22 02:01 | +10 stop | ZEC | DOWN | 0.52 | 0.64 | 0.85 |
| 10-22 02:01 | +20 | ZEC | DOWN | 0.52 | open |  |
| 10-22 02:01 | +15 | ZEC | DOWN | 0.52 | open |  |
| 10-22 02:01 | +10 | ZEC | DOWN | 0.52 | 0.64 | 0.85 |
