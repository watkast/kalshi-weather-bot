# Range-Scalp Bot

*Updated Wed Nov 18 01:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63375 | 55275 | 8100 (118) | 0 | $-17307.82 | -4.3% |
| **+10¢** | 47339 | 37859 | 9480 (159) | 1 | $-16221.83 | -5.5% |
| **+15¢** | 39689 | 29466 | 10223 (203) | 2 | $-14712.01 | -5.9% |
| **+20¢** | 35364 | 24637 | 10727 (258) | 2 | $-12945.93 | -5.8% |
| **+10¢ (15¢ stop)** | 77122 | 76964 | 158 (93) | 1 | $-28412.46 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 01:03 | +10 stop | XRP | DOWN | 0.67 | open |  |
| 11-18 01:03 | +20 | XRP | DOWN | 0.67 | open |  |
| 11-18 01:03 | +15 | XRP | DOWN | 0.66 | open |  |
| 11-18 01:03 | +10 | XRP | DOWN | 0.67 | open |  |
| 11-18 01:03 | +5 | XRP | DOWN | 0.67 | 0.73 | 0.30 |
| 11-18 01:02 | +10 stop | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 11-18 01:02 | +20 | NEAR | DOWN | 0.68 | open |  |
| 11-18 01:02 | +15 | NEAR | DOWN | 0.68 | open |  |
| 11-18 01:02 | +10 | NEAR | DOWN | 0.66 | 0.80 | 1.09 |
| 11-18 01:02 | +5 | NEAR | DOWN | 0.66 | 0.80 | 1.08 |
| 11-18 00:56 | +10 stop | ZEC | UP | 0.66 | 0.77 | 0.81 |
| 11-18 00:55 | +10 stop | ZEC | DOWN | 0.44 | 0.64 | 1.65 |
| 11-18 00:55 | +5 | BTC | UP | 0.69 | 0.85 | 1.36 |
| 11-18 00:53 | +10 stop | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 11-18 00:53 | +10 stop | SOL | DOWN | 0.65 | 0.78 | 1.01 |
| 11-18 00:52 | +10 stop | DOGE | UP | 0.33 | 0.58 | 2.16 |
| 11-18 00:52 | +10 stop | HYPE | DOWN | 0.58 | 0.72 | 1.07 |
| 11-18 00:52 | +10 stop | BTC | UP | 0.63 | 0.85 | 1.94 |
| 11-18 00:52 | +20 | BTC | UP | 0.63 | 0.85 | 1.94 |
| 11-18 00:52 | +15 | BTC | UP | 0.63 | 0.85 | 1.94 |
| 11-18 00:52 | +10 | BTC | UP | 0.63 | 0.85 | 1.94 |
| 11-18 00:52 | +5 | BTC | UP | 0.63 | 0.68 | 0.17 |
| 11-18 00:52 | +10 stop | XRP | DOWN | 0.69 | 0.82 | 1.04 |
| 11-18 00:52 | +10 stop | ZEC | UP | 0.57 | 0.30 | -3.03 |
| 11-18 00:52 | +15 | ZEC | UP | 0.57 | 0.77 | 1.69 |
| 11-18 00:52 | +10 | ZEC | UP | 0.57 | 0.77 | 1.69 |
| 11-18 00:52 | +5 | ZEC | UP | 0.57 | 0.64 | 0.35 |
| 11-18 00:52 | +5 | DOGE | UP | 0.54 | no | -5.58 |
| 11-18 00:51 | +5 | SOL | UP | 0.66 | no | -6.76 |
| 11-18 00:51 | +10 stop | XRP | UP | 0.59 | 0.41 | -2.14 |
| 11-18 00:51 | +5 | HYPE | UP | 0.62 | 0.68 | 0.27 |
| 11-18 00:50 | +10 stop | SOL | UP | 0.58 | 0.39 | -2.25 |
| 11-18 00:48 | +10 stop | BNB | UP | 0.56 | 0.28 | -3.13 |
| 11-18 00:48 | +10 stop | SOL | DOWN | 0.58 | 0.42 | -1.96 |
| 11-18 00:48 | +5 | BTC | UP | 0.68 | 0.74 | 0.30 |
| 11-18 00:48 | +10 stop | XRP | DOWN | 0.64 | 0.45 | -2.25 |
| 11-18 00:47 | +10 stop | HYPE | UP | 0.63 | 0.45 | -2.15 |
| 11-18 00:47 | +20 | HYPE | UP | 0.63 | 0.90 | 2.47 |
| 11-18 00:47 | +15 | HYPE | UP | 0.63 | 0.90 | 2.47 |
| 11-18 00:47 | +10 | HYPE | UP | 0.62 | 0.74 | 0.89 |
