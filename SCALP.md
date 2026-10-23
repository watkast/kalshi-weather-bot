# Range-Scalp Bot

*Updated Fri Oct 23 10:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30205 | 26300 | 3905 (39) | 0 | $-8865.58 | -4.7% |
| **+10¢** | 22636 | 18119 | 4517 (56) | 0 | $-7936.18 | -5.6% |
| **+15¢** | 18948 | 14090 | 4858 (79) | 1 | $-7174.47 | -6.0% |
| **+20¢** | 16773 | 11684 | 5089 (102) | 1 | $-6469.44 | -6.1% |
| **+10¢ (15¢ stop)** | 37055 | 36996 | 59 (32) | 0 | $-14018.64 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 10:57 | +10 stop | BTC | DOWN | 0.39 | 0.62 | 1.96 |
| 10-23 10:57 | +10 | BTC | DOWN | 0.39 | 0.62 | 1.96 |
| 10-23 10:57 | +5 | BTC | DOWN | 0.39 | 0.62 | 1.96 |
| 10-23 10:55 | +10 stop | BTC | UP | 0.55 | 0.29 | -2.93 |
| 10-23 10:54 | +5 | BTC | DOWN | 0.65 | 0.70 | 0.19 |
| 10-23 10:53 | +10 stop | BTC | DOWN | 0.67 | 0.44 | -2.64 |
| 10-23 10:52 | +5 | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-23 10:52 | +10 stop | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 10-23 10:52 | +10 stop | NEAR | DOWN | 0.61 | 0.80 | 1.61 |
| 10-23 10:52 | +10 stop | ETH | DOWN | 0.63 | 0.75 | 0.89 |
| 10-23 10:52 | +10 stop | ZEC | UP | 0.66 | 0.47 | -2.24 |
| 10-23 10:51 | +10 stop | SOL | UP | 0.60 | 0.34 | -2.96 |
| 10-23 10:50 | +10 stop | HYPE | DOWN | 0.62 | 0.80 | 1.54 |
| 10-23 10:49 | +10 stop | ETH | UP | 0.69 | 0.50 | -2.23 |
| 10-23 10:49 | +10 stop | DOGE | UP | 0.62 | 0.39 | -2.64 |
| 10-23 10:49 | +10 stop | SOL | UP | 0.71 | 0.54 | -2.03 |
| 10-23 10:49 | +10 stop | XRP | UP | 0.70 | 0.54 | -1.93 |
| 10-23 10:49 | +10 stop | BTC | UP | 0.71 | 0.56 | -1.83 |
| 10-23 10:49 | +10 stop | ZEC | UP | 0.58 | 0.77 | 1.59 |
| 10-23 10:48 | +5 | ETH | DOWN | 0.62 | 0.67 | 0.17 |
| 10-23 10:47 | +5 | HYPE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-23 10:47 | +10 stop | BTC | DOWN | 0.59 | 0.40 | -2.24 |
| 10-23 10:47 | +20 | BTC | DOWN | 0.59 | open |  |
| 10-23 10:47 | +15 | BTC | DOWN | 0.59 | open |  |
| 10-23 10:47 | +10 | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 10-23 10:47 | +5 | BTC | DOWN | 0.59 | 0.65 | 0.27 |
| 10-23 10:47 | +10 stop | ZEC | DOWN | 0.65 | 0.50 | -1.84 |
| 10-23 10:47 | +20 | ZEC | DOWN | 0.65 | 0.92 | 2.48 |
| 10-23 10:47 | +15 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-23 10:47 | +10 | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-23 10:47 | +5 | ZEC | DOWN | 0.65 | 0.70 | 0.19 |
| 10-23 10:47 | +10 stop | NEAR | DOWN | 0.62 | 0.44 | -2.15 |
| 10-23 10:47 | +20 | NEAR | DOWN | 0.62 | 0.82 | 1.72 |
| 10-23 10:47 | +15 | NEAR | DOWN | 0.62 | 0.80 | 1.51 |
| 10-23 10:47 | +10 | NEAR | DOWN | 0.62 | 0.80 | 1.51 |
| 10-23 10:47 | +5 | NEAR | DOWN | 0.62 | 0.80 | 1.51 |
| 10-23 10:47 | +10 stop | XRP | DOWN | 0.66 | 0.44 | -2.54 |
| 10-23 10:47 | +20 | XRP | DOWN | 0.66 | 0.88 | 1.96 |
| 10-23 10:47 | +15 | XRP | DOWN | 0.66 | 0.84 | 1.54 |
| 10-23 10:47 | +10 | XRP | DOWN | 0.66 | 0.79 | 1.02 |
