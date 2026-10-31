# Range-Scalp Bot

*Updated Sat Oct 31 08:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41981 | 36626 | 5355 (55) | 0 | $-11799.49 | -4.5% |
| **+10¢** | 31296 | 25095 | 6201 (79) | 1 | $-10571.92 | -5.4% |
| **+15¢** | 26164 | 19479 | 6685 (107) | 1 | $-9662.42 | -5.9% |
| **+20¢** | 23235 | 16234 | 7001 (138) | 1 | $-8514.69 | -5.8% |
| **+10¢ (15¢ stop)** | 51176 | 51101 | 75 (41) | 1 | $-19295.18 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 08:01 | +10 stop | NEAR | UP | 0.54 | open |  |
| 10-31 08:01 | +20 | NEAR | UP | 0.54 | open |  |
| 10-31 08:01 | +15 | NEAR | UP | 0.54 | open |  |
| 10-31 08:01 | +10 | NEAR | UP | 0.54 | open |  |
| 10-31 08:01 | +5 | NEAR | UP | 0.54 | 0.62 | 0.45 |
| 10-31 07:58 | +10 stop | DOGE | DOWN | 0.63 | 0.44 | -2.25 |
| 10-31 07:57 | +10 stop | DOGE | UP | 0.52 | 0.35 | -2.04 |
| 10-31 07:55 | +10 stop | SOL | UP | 0.66 | 0.77 | 0.81 |
| 10-31 07:55 | +15 | SOL | UP | 0.65 | 0.80 | 1.22 |
| 10-31 07:55 | +10 | SOL | UP | 0.66 | 0.77 | 0.81 |
| 10-31 07:54 | +10 stop | NEAR | UP | 0.62 | 0.75 | 0.99 |
| 10-31 07:54 | +5 | NEAR | UP | 0.59 | 0.67 | 0.47 |
| 10-31 07:53 | +10 stop | BNB | DOWN | 0.59 | 0.13 | -4.85 |
| 10-31 07:53 | +10 stop | ETH | UP | 0.61 | 0.78 | 1.40 |
| 10-31 07:52 | +10 stop | BTC | UP | 0.68 | 0.78 | 0.71 |
| 10-31 07:52 | +5 | NEAR | DOWN | 0.54 | 0.62 | 0.45 |
| 10-31 07:52 | +10 stop | HYPE | UP | 0.64 | 0.79 | 1.17 |
| 10-31 07:52 | +10 stop | NEAR | DOWN | 0.55 | 0.40 | -1.85 |
| 10-31 07:52 | +5 | NEAR | DOWN | 0.55 | 0.60 | 0.15 |
| 10-31 07:51 | +10 stop | DOGE | DOWN | 0.57 | 0.70 | 0.97 |
| 10-31 07:51 | +10 stop | SOL | UP | 0.67 | 0.80 | 1.02 |
| 10-31 07:51 | +20 | SOL | UP | 0.66 | no | -6.76 |
| 10-31 07:51 | +15 | SOL | UP | 0.66 | 0.82 | 1.33 |
| 10-31 07:50 | +10 | SOL | UP | 0.65 | 0.80 | 1.22 |
| 10-31 07:50 | +10 stop | BTC | UP | 0.53 | 0.65 | 0.86 |
| 10-31 07:50 | +5 | HYPE | DOWN | 0.67 | yes | -6.91 |
| 10-31 07:49 | +10 stop | NEAR | DOWN | 0.54 | 0.64 | 0.65 |
| 10-31 07:49 | +20 | NEAR | DOWN | 0.54 | yes | -5.58 |
| 10-31 07:49 | +15 | NEAR | DOWN | 0.55 | yes | -5.68 |
| 10-31 07:49 | +10 | NEAR | DOWN | 0.55 | yes | -5.68 |
| 10-31 07:49 | +5 | NEAR | DOWN | 0.55 | 0.64 | 0.55 |
| 10-31 07:49 | +10 stop | SOL | UP | 0.54 | 0.68 | 1.06 |
| 10-31 07:48 | +10 | XRP | UP | 0.55 | 0.70 | 1.17 |
| 10-31 07:48 | +5 | XRP | UP | 0.55 | 0.70 | 1.17 |
| 10-31 07:48 | +5 | BTC | DOWN | 0.58 | 0.76 | 1.49 |
| 10-31 07:48 | +10 stop | ETH | DOWN | 0.63 | 0.41 | -2.54 |
| 10-31 07:48 | +10 stop | SOL | DOWN | 0.53 | 0.65 | 0.86 |
| 10-31 07:48 | +10 stop | XRP | UP | 0.53 | 0.70 | 1.37 |
| 10-31 07:48 | +20 | XRP | UP | 0.52 | 0.74 | 1.88 |
| 10-31 07:48 | +15 | XRP | UP | 0.53 | 0.70 | 1.38 |
