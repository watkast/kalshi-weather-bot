# Range-Scalp Bot

*Updated Thu Oct 29 21:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39716 | 34678 | 5038 (50) | 2 | $-10993.24 | -4.4% |
| **+10¢** | 29606 | 23779 | 5827 (73) | 2 | $-9749.58 | -5.2% |
| **+15¢** | 24755 | 18487 | 6268 (100) | 2 | $-8756.15 | -5.6% |
| **+20¢** | 21967 | 15401 | 6566 (129) | 3 | $-7631.72 | -5.5% |
| **+10¢ (15¢ stop)** | 48502 | 48432 | 70 (37) | 0 | $-18392.59 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 21:10 | +10 stop | ETH | UP | 0.68 | 0.46 | -2.54 |
| 10-29 21:10 | +10 stop | NEAR | UP | 0.64 | 0.75 | 0.79 |
| 10-29 21:10 | +5 | ETH | UP | 0.69 | 0.81 | 0.94 |
| 10-29 21:10 | +10 stop | HYPE | DOWN | 0.59 | 0.80 | 1.77 |
| 10-29 21:10 | +15 | HYPE | DOWN | 0.61 | 0.80 | 1.61 |
| 10-29 21:10 | +10 | HYPE | DOWN | 0.61 | 0.80 | 1.61 |
| 10-29 21:10 | +5 | HYPE | DOWN | 0.61 | 0.80 | 1.61 |
| 10-29 21:09 | +5 | ZEC | UP | 0.58 | 0.76 | 1.49 |
| 10-29 21:09 | +10 stop | ZEC | UP | 0.58 | 0.76 | 1.49 |
| 10-29 21:08 | +10 stop | SOL | UP | 0.66 | 0.78 | 0.91 |
| 10-29 21:08 | +10 stop | ETH | UP | 0.54 | 0.65 | 0.76 |
| 10-29 21:07 | +10 | XRP | UP | 0.70 | 0.81 | 0.84 |
| 10-29 21:07 | +10 stop | DOGE | UP | 0.65 | 0.77 | 0.91 |
| 10-29 21:07 | +10 stop | ZEC | DOWN | 0.63 | 0.42 | -2.45 |
| 10-29 21:07 | +10 stop | XRP | UP | 0.61 | 0.73 | 0.89 |
| 10-29 21:07 | +10 stop | NEAR | DOWN | 0.66 | 0.48 | -2.14 |
| 10-29 21:07 | +15 | NEAR | DOWN | 0.66 | open |  |
| 10-29 21:07 | +10 | NEAR | DOWN | 0.67 | open |  |
| 10-29 21:07 | +5 | NEAR | DOWN | 0.66 | open |  |
| 10-29 21:06 | +10 stop | BNB | UP | 0.56 | 0.70 | 1.07 |
| 10-29 21:06 | +20 | BNB | UP | 0.56 | 0.79 | 2.00 |
| 10-29 21:06 | +15 | BNB | UP | 0.56 | 0.75 | 1.58 |
| 10-29 21:06 | +10 | BNB | UP | 0.56 | 0.70 | 1.07 |
| 10-29 21:06 | +5 | BNB | UP | 0.56 | 0.61 | 0.15 |
| 10-29 21:06 | +10 stop | ETH | DOWN | 0.63 | 0.48 | -1.85 |
| 10-29 21:05 | +10 stop | SOL | DOWN | 0.69 | 0.47 | -2.53 |
| 10-29 21:05 | +10 stop | BTC | UP | 0.71 | 0.84 | 1.05 |
| 10-29 21:04 | +10 stop | ETH | DOWN | 0.67 | 0.52 | -1.84 |
| 10-29 21:04 | +20 | ETH | DOWN | 0.66 | open |  |
| 10-29 21:04 | +15 | ETH | DOWN | 0.66 | open |  |
| 10-29 21:04 | +10 | ETH | DOWN | 0.66 | open |  |
| 10-29 21:04 | +10 stop | DOGE | DOWN | 0.68 | 0.42 | -2.94 |
| 10-29 21:04 | +10 stop | XRP | DOWN | 0.62 | 0.45 | -2.05 |
| 10-29 21:04 | +5 | XRP | DOWN | 0.68 | open |  |
| 10-29 21:03 | +10 stop | SOL | DOWN | 0.66 | 0.78 | 0.91 |
| 10-29 21:03 | +10 stop | BNB | DOWN | 0.60 | 0.72 | 0.83 |
| 10-29 21:03 | +10 stop | NEAR | DOWN | 0.70 | 0.84 | 1.15 |
| 10-29 21:03 | +10 stop | HYPE | DOWN | 0.65 | 0.83 | 1.54 |
| 10-29 21:03 | +20 | HYPE | DOWN | 0.65 | open |  |
| 10-29 21:03 | +15 | HYPE | DOWN | 0.65 | 0.83 | 1.54 |
