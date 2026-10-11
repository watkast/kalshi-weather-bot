# Range-Scalp Bot

*Updated Sun Oct 11 22:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12636 | 10910 | 1726 (25) | 3 | $-4153.86 | -5.2% |
| **+10¢** | 9585 | 7586 | 1999 (37) | 3 | $-3898.18 | -6.5% |
| **+15¢** | 8065 | 5938 | 2127 (55) | 5 | $-3358.53 | -6.6% |
| **+20¢** | 7189 | 4971 | 2218 (69) | 5 | $-2861.37 | -6.3% |
| **+10¢ (15¢ stop)** | 15559 | 15518 | 41 (25) | 0 | $-6070.46 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 22:55 | +10 stop | BNB | DOWN | 0.48 | 0.59 | 0.76 |
| 10-11 22:55 | +5 | BNB | DOWN | 0.48 | 0.59 | 0.76 |
| 10-11 22:53 | +10 stop | HYPE | DOWN | 0.60 | 0.72 | 0.88 |
| 10-11 22:53 | +10 | HYPE | DOWN | 0.60 | 0.72 | 0.88 |
| 10-11 22:53 | +5 | HYPE | DOWN | 0.60 | 0.72 | 0.88 |
| 10-11 22:52 | +10 stop | BNB | DOWN | 0.50 | 0.35 | -1.84 |
| 10-11 22:52 | +10 stop | HYPE | DOWN | 0.55 | 0.67 | 0.86 |
| 10-11 22:52 | +10 | HYPE | DOWN | 0.55 | 0.67 | 0.86 |
| 10-11 22:52 | +5 | HYPE | DOWN | 0.55 | 0.67 | 0.86 |
| 10-11 22:51 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-11 22:51 | +10 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-11 22:51 | +10 stop | NEAR | DOWN | 0.54 | 0.29 | -2.83 |
| 10-11 22:51 | +5 | NEAR | DOWN | 0.55 | open |  |
| 10-11 22:50 | +5 | BTC | DOWN | 0.65 | 0.79 | 1.12 |
| 10-11 22:50 | +10 stop | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 10-11 22:50 | +15 | ETH | DOWN | 0.66 | open |  |
| 10-11 22:50 | +10 | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 10-11 22:50 | +5 | ETH | DOWN | 0.65 | 0.73 | 0.50 |
| 10-11 22:49 | +10 stop | NEAR | UP | 0.58 | 0.43 | -1.86 |
| 10-11 22:49 | +5 | BTC | DOWN | 0.58 | 0.63 | 0.15 |
| 10-11 22:49 | +10 stop | ETH | DOWN | 0.52 | 0.68 | 1.26 |
| 10-11 22:49 | +20 | ETH | DOWN | 0.52 | 0.73 | 1.78 |
| 10-11 22:49 | +15 | ETH | DOWN | 0.52 | 0.68 | 1.26 |
| 10-11 22:49 | +10 | ETH | DOWN | 0.52 | 0.68 | 1.26 |
| 10-11 22:49 | +5 | ETH | DOWN | 0.52 | 0.58 | 0.24 |
| 10-11 22:49 | +10 stop | HYPE | DOWN | 0.68 | 0.79 | 0.82 |
| 10-11 22:49 | +10 | HYPE | DOWN | 0.68 | 0.79 | 0.82 |
| 10-11 22:49 | +5 | HYPE | DOWN | 0.68 | 0.76 | 0.51 |
| 10-11 22:49 | +10 stop | ZEC | UP | 0.62 | 0.78 | 1.30 |
| 10-11 22:49 | +10 | ZEC | UP | 0.62 | 0.78 | 1.30 |
| 10-11 22:49 | +5 | ZEC | UP | 0.62 | 0.69 | 0.38 |
| 10-11 22:49 | +5 | NEAR | UP | 0.53 | 0.58 | 0.14 |
| 10-11 22:48 | +10 stop | NEAR | UP | 0.67 | 0.50 | -2.04 |
| 10-11 22:48 | +20 | NEAR | UP | 0.66 | open |  |
| 10-11 22:48 | +15 | NEAR | UP | 0.66 | open |  |
| 10-11 22:48 | +10 | NEAR | UP | 0.64 | open |  |
| 10-11 22:48 | +5 | NEAR | UP | 0.60 | 0.65 | 0.17 |
| 10-11 22:48 | +10 stop | SOL | DOWN | 0.65 | 0.78 | 1.01 |
| 10-11 22:48 | +10 stop | XRP | DOWN | 0.64 | 0.76 | 0.90 |
| 10-11 22:48 | +10 stop | BTC | DOWN | 0.57 | 0.67 | 0.66 |
