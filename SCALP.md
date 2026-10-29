# Range-Scalp Bot

*Updated Thu Oct 29 09:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39069 | 34097 | 4972 (49) | 4 | $-10943.65 | -4.4% |
| **+10¢** | 29143 | 23405 | 5738 (71) | 6 | $-9658.67 | -5.3% |
| **+15¢** | 24370 | 18205 | 6165 (98) | 7 | $-8616.70 | -5.6% |
| **+20¢** | 21619 | 15158 | 6461 (127) | 7 | $-7526.57 | -5.5% |
| **+10¢ (15¢ stop)** | 47770 | 47703 | 67 (35) | 2 | $-18127.29 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 09:42 | +10 stop | DOGE | DOWN | 0.64 | open |  |
| 10-29 09:42 | +20 | DOGE | DOWN | 0.64 | open |  |
| 10-29 09:42 | +15 | DOGE | DOWN | 0.64 | open |  |
| 10-29 09:42 | +10 | DOGE | DOWN | 0.64 | open |  |
| 10-29 09:42 | +5 | DOGE | DOWN | 0.64 | 0.73 | 0.59 |
| 10-29 09:42 | +10 stop | SOL | UP | 0.59 | open |  |
| 10-29 09:42 | +10 stop | ZEC | DOWN | 0.61 | 0.72 | 0.78 |
| 10-29 09:42 | +20 | ZEC | DOWN | 0.61 | open |  |
| 10-29 09:42 | +15 | ZEC | DOWN | 0.61 | open |  |
| 10-29 09:42 | +10 | ZEC | DOWN | 0.62 | 0.72 | 0.71 |
| 10-29 09:42 | +5 | ZEC | DOWN | 0.60 | 0.72 | 0.88 |
| 10-29 09:42 | +10 stop | ETH | UP | 0.57 | 0.67 | 0.66 |
| 10-29 09:40 | +10 stop | ETH | UP | 0.69 | 0.82 | 1.05 |
| 10-29 09:40 | +10 stop | SOL | UP | 0.65 | 0.76 | 0.81 |
| 10-29 09:40 | +10 stop | ZEC | UP | 0.56 | 0.68 | 0.86 |
| 10-29 09:40 | +20 | ZEC | UP | 0.56 | 0.79 | 2.00 |
| 10-29 09:40 | +15 | ZEC | UP | 0.56 | 0.72 | 1.27 |
| 10-29 09:40 | +10 | ZEC | UP | 0.56 | 0.68 | 0.86 |
| 10-29 09:40 | +5 | ZEC | UP | 0.56 | 0.68 | 0.86 |
| 10-29 09:40 | +10 stop | NEAR | UP | 0.69 | 0.81 | 0.94 |
| 10-29 09:39 | +5 | ETH | DOWN | 0.70 | open |  |
| 10-29 09:39 | +5 | SOL | DOWN | 0.66 | open |  |
| 10-29 09:38 | +10 stop | SOL | DOWN | 0.63 | 0.32 | -3.43 |
| 10-29 09:38 | +20 | SOL | DOWN | 0.63 | open |  |
| 10-29 09:38 | +15 | SOL | DOWN | 0.63 | open |  |
| 10-29 09:38 | +10 | SOL | DOWN | 0.63 | open |  |
| 10-29 09:38 | +5 | SOL | DOWN | 0.63 | 0.68 | 0.17 |
| 10-29 09:38 | +10 stop | HYPE | UP | 0.63 | 0.77 | 1.10 |
| 10-29 09:38 | +5 | HYPE | UP | 0.65 | 0.77 | 0.94 |
| 10-29 09:38 | +10 stop | ETH | DOWN | 0.62 | 0.39 | -2.64 |
| 10-29 09:38 | +15 | ETH | DOWN | 0.61 | open |  |
| 10-29 09:38 | +10 | ETH | DOWN | 0.61 | open |  |
| 10-29 09:38 | +5 | ETH | DOWN | 0.61 | 0.67 | 0.27 |
| 10-29 09:38 | +5 | NEAR | DOWN | 0.59 | open |  |
| 10-29 09:38 | +5 | BTC | DOWN | 0.64 | open |  |
| 10-29 09:38 | +5 | HYPE | DOWN | 0.59 | 0.65 | 0.23 |
| 10-29 09:36 | +10 stop | BTC | DOWN | 0.66 | 0.29 | -4.01 |
| 10-29 09:36 | +10 | BTC | DOWN | 0.67 | open |  |
| 10-29 09:36 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 10-29 09:36 | +5 | HYPE | DOWN | 0.62 | 0.70 | 0.51 |
