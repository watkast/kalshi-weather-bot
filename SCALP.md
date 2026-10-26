# Range-Scalp Bot

*Updated Mon Oct 26 04:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34244 | 29906 | 4338 (43) | 1 | $-9407.61 | -4.4% |
| **+10¢** | 25630 | 20609 | 5021 (65) | 1 | $-8262.06 | -5.1% |
| **+15¢** | 21431 | 16024 | 5407 (89) | 1 | $-7390.34 | -5.5% |
| **+20¢** | 18994 | 13332 | 5662 (111) | 4 | $-6467.29 | -5.4% |
| **+10¢ (15¢ stop)** | 41942 | 41880 | 62 (33) | 0 | $-15961.92 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 04:02 | +10 stop | SOL | UP | 0.69 | 0.79 | 0.73 |
| 10-26 04:02 | +20 | SOL | UP | 0.69 | open |  |
| 10-26 04:02 | +15 | SOL | UP | 0.69 | 0.85 | 1.36 |
| 10-26 04:02 | +10 | SOL | UP | 0.69 | 0.79 | 0.73 |
| 10-26 04:02 | +5 | SOL | UP | 0.69 | 0.75 | 0.31 |
| 10-26 04:02 | +10 stop | BTC | UP | 0.70 | 0.85 | 1.26 |
| 10-26 04:01 | +10 stop | HYPE | UP | 0.69 | 0.81 | 0.90 |
| 10-26 04:01 | +20 | HYPE | UP | 0.69 | open |  |
| 10-26 04:01 | +15 | HYPE | UP | 0.69 | 0.86 | 1.42 |
| 10-26 04:01 | +10 | HYPE | UP | 0.69 | 0.81 | 0.90 |
| 10-26 04:01 | +5 | HYPE | UP | 0.69 | 0.78 | 0.58 |
| 10-26 04:01 | +10 stop | ETH | UP | 0.69 | 0.82 | 1.04 |
| 10-26 04:01 | +20 | ETH | UP | 0.69 | open |  |
| 10-26 04:01 | +15 | ETH | UP | 0.69 | 0.86 | 1.46 |
| 10-26 04:01 | +10 | ETH | UP | 0.69 | 0.82 | 1.04 |
| 10-26 04:01 | +5 | ETH | UP | 0.69 | 0.74 | 0.21 |
| 10-26 04:01 | +10 stop | BTC | DOWN | 0.54 | 0.34 | -2.34 |
| 10-26 04:01 | +20 | BTC | DOWN | 0.54 | open |  |
| 10-26 04:01 | +15 | BTC | DOWN | 0.55 | open |  |
| 10-26 04:01 | +10 | BTC | DOWN | 0.55 | open |  |
| 10-26 04:01 | +5 | BTC | DOWN | 0.55 | open |  |
| 10-26 03:57 | +10 stop | NEAR | UP | 0.71 | 0.87 | 1.37 |
| 10-26 03:55 | +10 stop | NEAR | DOWN | 0.71 | 0.54 | -2.03 |
| 10-26 03:55 | +20 | NEAR | DOWN | 0.71 | yes | -7.25 |
| 10-26 03:55 | +15 | NEAR | DOWN | 0.71 | yes | -7.25 |
| 10-26 03:55 | +10 | NEAR | DOWN | 0.71 | yes | -7.25 |
| 10-26 03:55 | +5 | NEAR | DOWN | 0.71 | yes | -7.25 |
| 10-26 03:51 | +10 stop | HYPE | DOWN | 0.61 | 0.75 | 1.09 |
| 10-26 03:51 | +15 | HYPE | DOWN | 0.61 | 0.76 | 1.20 |
| 10-26 03:51 | +10 | HYPE | DOWN | 0.60 | 0.75 | 1.15 |
| 10-26 03:51 | +5 | HYPE | DOWN | 0.60 | 0.66 | 0.23 |
| 10-26 03:50 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 10-26 03:49 | +5 | DOGE | DOWN | 0.67 | 0.76 | 0.61 |
| 10-26 03:49 | +5 | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-26 03:49 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-26 03:49 | +10 stop | BNB | DOWN | 0.62 | 0.78 | 1.30 |
| 10-26 03:48 | +5 | ZEC | DOWN | 0.62 | 0.71 | 0.58 |
| 10-26 03:48 | +10 stop | DOGE | DOWN | 0.56 | 0.66 | 0.71 |
| 10-26 03:48 | +20 | DOGE | DOWN | 0.56 | 0.76 | 1.74 |
| 10-26 03:48 | +15 | DOGE | DOWN | 0.56 | 0.76 | 1.74 |
