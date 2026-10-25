# Range-Scalp Bot

*Updated Sun Oct 25 08:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32890 | 28689 | 4201 (42) | 1 | $-9289.10 | -4.5% |
| **+10¢** | 24620 | 19754 | 4866 (60) | 0 | $-8293.37 | -5.4% |
| **+15¢** | 20609 | 15372 | 5237 (83) | 0 | $-7459.97 | -5.8% |
| **+20¢** | 18262 | 12780 | 5482 (105) | 0 | $-6585.85 | -5.7% |
| **+10¢ (15¢ stop)** | 40372 | 40312 | 60 (32) | 0 | $-15401.81 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 08:49 | +10 stop | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-25 08:49 | +20 | BTC | DOWN | 0.70 | 0.91 | 1.89 |
| 10-25 08:49 | +15 | BTC | DOWN | 0.70 | 0.86 | 1.36 |
| 10-25 08:49 | +10 | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-25 08:48 | +5 | BTC | UP | 0.51 | open |  |
| 10-25 08:48 | +10 stop | HYPE | UP | 0.60 | 0.39 | -2.44 |
| 10-25 08:47 | +5 | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-25 08:47 | +5 | ETH | DOWN | 0.61 | 0.73 | 0.89 |
| 10-25 08:47 | +5 | XRP | DOWN | 0.65 | 0.71 | 0.29 |
| 10-25 08:47 | +5 | ZEC | DOWN | 0.59 | 0.71 | 0.88 |
| 10-25 08:47 | +5 | BNB | DOWN | 0.63 | 0.69 | 0.28 |
| 10-25 08:47 | +5 | ETH | DOWN | 0.59 | 0.66 | 0.37 |
| 10-25 08:47 | +10 stop | BTC | DOWN | 0.49 | 0.69 | 1.67 |
| 10-25 08:47 | +20 | BTC | DOWN | 0.49 | 0.69 | 1.67 |
| 10-25 08:47 | +15 | BTC | DOWN | 0.49 | 0.69 | 1.67 |
| 10-25 08:47 | +10 | BTC | DOWN | 0.49 | 0.69 | 1.67 |
| 10-25 08:47 | +5 | BTC | DOWN | 0.49 | 0.57 | 0.44 |
| 10-25 08:46 | +10 stop | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 10-25 08:46 | +20 | XRP | DOWN | 0.61 | 0.82 | 1.82 |
| 10-25 08:46 | +15 | XRP | DOWN | 0.61 | 0.82 | 1.82 |
| 10-25 08:46 | +10 | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 10-25 08:46 | +5 | XRP | DOWN | 0.61 | 0.67 | 0.27 |
| 10-25 08:46 | +10 stop | HYPE | DOWN | 0.59 | 0.44 | -1.89 |
| 10-25 08:46 | +20 | HYPE | DOWN | 0.59 | 0.80 | 1.77 |
| 10-25 08:46 | +15 | HYPE | DOWN | 0.59 | 0.76 | 1.36 |
| 10-25 08:46 | +10 | HYPE | DOWN | 0.59 | 0.76 | 1.36 |
| 10-25 08:46 | +5 | HYPE | DOWN | 0.59 | 0.66 | 0.33 |
| 10-25 08:46 | +10 stop | SOL | DOWN | 0.62 | 0.78 | 1.30 |
| 10-25 08:46 | +20 | SOL | DOWN | 0.62 | 0.83 | 1.83 |
| 10-25 08:46 | +15 | SOL | DOWN | 0.62 | 0.78 | 1.30 |
| 10-25 08:46 | +10 | SOL | DOWN | 0.62 | 0.78 | 1.30 |
| 10-25 08:46 | +5 | SOL | DOWN | 0.62 | 0.68 | 0.27 |
| 10-25 08:46 | +10 stop | NEAR | DOWN | 0.62 | 0.81 | 1.62 |
| 10-25 08:46 | +20 | NEAR | DOWN | 0.62 | 0.84 | 1.93 |
| 10-25 08:46 | +15 | NEAR | DOWN | 0.62 | 0.81 | 1.62 |
| 10-25 08:46 | +10 | NEAR | DOWN | 0.62 | 0.81 | 1.62 |
| 10-25 08:46 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 10-25 08:46 | +10 stop | ZEC | DOWN | 0.56 | 0.71 | 1.17 |
| 10-25 08:46 | +20 | ZEC | DOWN | 0.56 | 0.78 | 1.89 |
| 10-25 08:46 | +15 | ZEC | DOWN | 0.56 | 0.71 | 1.17 |
