# Range-Scalp Bot

*Updated Mon Nov 16 04:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61707 | 53849 | 7858 (115) | 2 | $-16584.29 | -4.3% |
| **+10¢** | 46095 | 36886 | 9209 (157) | 0 | $-15531.56 | -5.4% |
| **+15¢** | 38625 | 28691 | 9934 (196) | 0 | $-14160.00 | -5.8% |
| **+20¢** | 34433 | 24014 | 10419 (249) | 0 | $-12374.26 | -5.7% |
| **+10¢ (15¢ stop)** | 75095 | 74941 | 154 (90) | 0 | $-27636.69 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 04:39 | +10 stop | ZEC | UP | 0.64 | 0.40 | -2.74 |
| 11-16 04:39 | +5 | ZEC | UP | 0.65 | open |  |
| 11-16 04:38 | +10 stop | HYPE | UP | 0.62 | 0.43 | -2.25 |
| 11-16 04:38 | +5 | HYPE | UP | 0.69 | open |  |
| 11-16 04:37 | +10 stop | ZEC | DOWN | 0.51 | 0.63 | 0.85 |
| 11-16 04:37 | +5 | ZEC | DOWN | 0.51 | 0.63 | 0.85 |
| 11-16 04:36 | +10 stop | HYPE | DOWN | 0.55 | 0.38 | -2.06 |
| 11-16 04:36 | +10 | HYPE | DOWN | 0.55 | 0.66 | 0.75 |
| 11-16 04:36 | +5 | HYPE | DOWN | 0.56 | 0.63 | 0.35 |
| 11-16 04:33 | +10 stop | XRP | DOWN | 0.69 | 0.82 | 1.04 |
| 11-16 04:33 | +20 | XRP | DOWN | 0.69 | 0.90 | 1.88 |
| 11-16 04:33 | +15 | XRP | DOWN | 0.69 | 0.84 | 1.25 |
| 11-16 04:33 | +10 | XRP | DOWN | 0.69 | 0.82 | 1.04 |
| 11-16 04:33 | +5 | XRP | DOWN | 0.69 | 0.75 | 0.31 |
| 11-16 04:33 | +10 stop | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 11-16 04:33 | +20 | BNB | DOWN | 0.65 | 0.87 | 1.96 |
| 11-16 04:33 | +15 | BNB | DOWN | 0.65 | 0.80 | 1.22 |
| 11-16 04:33 | +10 | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 11-16 04:33 | +5 | BNB | DOWN | 0.65 | 0.72 | 0.39 |
| 11-16 04:32 | +10 stop | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-16 04:31 | +10 stop | HYPE | DOWN | 0.66 | 0.78 | 0.91 |
| 11-16 04:31 | +20 | HYPE | DOWN | 0.66 | 0.88 | 1.96 |
| 11-16 04:31 | +15 | HYPE | DOWN | 0.66 | 0.88 | 1.96 |
| 11-16 04:31 | +10 | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-16 04:31 | +5 | HYPE | DOWN | 0.67 | 0.72 | 0.19 |
| 11-16 04:30 | +10 stop | BTC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-16 04:30 | +20 | BTC | DOWN | 0.70 | 0.93 | 2.05 |
| 11-16 04:30 | +15 | BTC | DOWN | 0.70 | 0.88 | 1.57 |
| 11-16 04:30 | +10 | BTC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-16 04:30 | +5 | BTC | DOWN | 0.70 | 0.77 | 0.42 |
| 11-16 04:30 | +10 stop | ZEC | DOWN | 0.70 | 0.55 | -1.83 |
| 11-16 04:30 | +20 | ZEC | DOWN | 0.70 | 0.91 | 1.86 |
| 11-16 04:30 | +15 | ZEC | DOWN | 0.70 | 0.91 | 1.86 |
| 11-16 04:30 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-16 04:30 | +5 | ZEC | DOWN | 0.70 | 0.77 | 0.42 |
| 11-16 04:26 | +10 stop | ZEC | UP | 0.68 | 0.88 | 1.76 |
| 11-16 04:26 | +5 | ZEC | UP | 0.68 | 0.88 | 1.76 |
| 11-16 04:23 | +10 stop | ZEC | UP | 0.65 | 0.78 | 1.01 |
| 11-16 04:23 | +10 stop | HYPE | UP | 0.68 | 0.86 | 1.55 |
| 11-16 04:22 | +10 stop | NEAR | UP | 0.65 | 0.77 | 0.91 |
