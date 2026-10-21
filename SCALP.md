# Range-Scalp Bot

*Updated Wed Oct 21 19:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27611 | 24044 | 3567 (39) | 0 | $-8039.27 | -4.6% |
| **+10¢** | 20763 | 16645 | 4118 (55) | 0 | $-7075.77 | -5.4% |
| **+15¢** | 17390 | 12957 | 4433 (78) | 0 | $-6327.05 | -5.8% |
| **+20¢** | 15393 | 10747 | 4646 (98) | 1 | $-5677.90 | -5.9% |
| **+10¢ (15¢ stop)** | 33874 | 33815 | 59 (32) | 0 | $-12585.91 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 19:01 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-21 19:01 | +10 stop | BNB | DOWN | 0.62 | 0.77 | 1.20 |
| 10-21 19:01 | +20 | BNB | DOWN | 0.60 | 0.81 | 1.82 |
| 10-21 19:01 | +15 | BNB | DOWN | 0.60 | 0.77 | 1.40 |
| 10-21 19:01 | +10 | BNB | DOWN | 0.60 | 0.77 | 1.40 |
| 10-21 19:01 | +5 | BNB | DOWN | 0.61 | 0.67 | 0.27 |
| 10-21 19:01 | +10 stop | BTC | DOWN | 0.59 | 0.82 | 2.02 |
| 10-21 19:01 | +20 | BTC | DOWN | 0.59 | 0.82 | 2.02 |
| 10-21 19:01 | +15 | BTC | DOWN | 0.60 | 0.82 | 1.92 |
| 10-21 19:01 | +10 | BTC | DOWN | 0.59 | 0.82 | 2.02 |
| 10-21 19:01 | +5 | BTC | DOWN | 0.59 | 0.66 | 0.37 |
| 10-21 19:01 | +10 stop | ZEC | DOWN | 0.55 | 0.76 | 1.79 |
| 10-21 19:01 | +20 | ZEC | DOWN | 0.55 | 0.76 | 1.79 |
| 10-21 19:01 | +15 | ZEC | DOWN | 0.55 | 0.76 | 1.79 |
| 10-21 19:01 | +10 | ZEC | DOWN | 0.54 | 0.64 | 0.65 |
| 10-21 19:01 | +5 | ZEC | DOWN | 0.54 | 0.60 | 0.25 |
| 10-21 19:01 | +10 stop | SOL | DOWN | 0.69 | 0.82 | 1.04 |
| 10-21 19:01 | +20 | SOL | DOWN | 0.69 | open |  |
| 10-21 19:01 | +15 | SOL | DOWN | 0.69 | 0.86 | 1.46 |
| 10-21 19:01 | +10 | SOL | DOWN | 0.69 | 0.82 | 1.04 |
| 10-21 19:01 | +5 | SOL | DOWN | 0.69 | 0.82 | 1.04 |
| 10-21 19:01 | +10 stop | XRP | DOWN | 0.59 | 0.71 | 0.88 |
| 10-21 19:01 | +20 | XRP | DOWN | 0.59 | 0.84 | 2.23 |
| 10-21 19:01 | +15 | XRP | DOWN | 0.60 | 0.84 | 2.13 |
| 10-21 19:01 | +10 | XRP | DOWN | 0.60 | 0.71 | 0.78 |
| 10-21 19:01 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 10-21 18:50 | +10 stop | NEAR | DOWN | 0.63 | 0.81 | 1.52 |
| 10-21 18:50 | +10 | NEAR | DOWN | 0.63 | 0.81 | 1.52 |
| 10-21 18:49 | +10 stop | HYPE | DOWN | 0.67 | 0.81 | 1.09 |
| 10-21 18:49 | +10 | HYPE | DOWN | 0.66 | 0.81 | 1.19 |
| 10-21 18:49 | +5 | HYPE | DOWN | 0.66 | 0.72 | 0.25 |
| 10-21 18:48 | +10 stop | XRP | DOWN | 0.70 | 0.83 | 1.05 |
| 10-21 18:48 | +20 | XRP | DOWN | 0.70 | 0.94 | 2.15 |
| 10-21 18:48 | +15 | XRP | DOWN | 0.70 | 0.94 | 2.15 |
| 10-21 18:48 | +10 | XRP | DOWN | 0.70 | 0.83 | 1.05 |
| 10-21 18:48 | +5 | XRP | DOWN | 0.70 | 0.79 | 0.63 |
| 10-21 18:48 | +10 stop | SOL | DOWN | 0.60 | 0.78 | 1.50 |
| 10-21 18:48 | +10 stop | NEAR | UP | 0.48 | 0.60 | 0.88 |
| 10-21 18:48 | +10 | NEAR | UP | 0.47 | 0.60 | 0.95 |
| 10-21 18:47 | +10 stop | SOL | UP | 0.63 | 0.46 | -2.05 |
