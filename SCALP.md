# Range-Scalp Bot

*Updated Fri Oct 30 06:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40352 | 35234 | 5118 (51) | 6 | $-11171.34 | -4.4% |
| **+10¢** | 30061 | 24140 | 5921 (74) | 7 | $-9931.44 | -5.3% |
| **+15¢** | 25139 | 18769 | 6370 (101) | 7 | $-8921.20 | -5.7% |
| **+20¢** | 22308 | 15631 | 6677 (130) | 8 | $-7836.81 | -5.6% |
| **+10¢ (15¢ stop)** | 49237 | 49167 | 70 (37) | 0 | $-18646.73 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 06:55 | +10 stop | BTC | DOWN | 0.52 | 0.30 | -2.53 |
| 10-30 06:55 | +10 stop | DOGE | DOWN | 0.54 | 0.39 | -1.85 |
| 10-30 06:53 | +10 stop | HYPE | UP | 0.57 | 0.79 | 1.86 |
| 10-30 06:53 | +10 stop | HYPE | UP | 0.54 | 0.64 | 0.65 |
| 10-30 06:53 | +10 stop | BTC | UP | 0.60 | 0.40 | -2.34 |
| 10-30 06:52 | +5 | BTC | UP | 0.67 | 0.78 | 0.81 |
| 10-30 06:52 | +10 stop | DOGE | DOWN | 0.62 | 0.45 | -2.05 |
| 10-30 06:52 | +20 | DOGE | DOWN | 0.62 | open |  |
| 10-30 06:52 | +15 | DOGE | DOWN | 0.62 | open |  |
| 10-30 06:52 | +10 | DOGE | DOWN | 0.62 | open |  |
| 10-30 06:52 | +5 | DOGE | DOWN | 0.62 | open |  |
| 10-30 06:52 | +10 stop | BNB | UP | 0.66 | 0.77 | 0.81 |
| 10-30 06:52 | +10 stop | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 10-30 06:52 | +10 stop | XRP | UP | 0.67 | 0.86 | 1.61 |
| 10-30 06:51 | +10 stop | BTC | DOWN | 0.55 | 0.36 | -2.25 |
| 10-30 06:51 | +10 | BTC | DOWN | 0.55 | open |  |
| 10-30 06:51 | +5 | BTC | DOWN | 0.55 | 0.61 | 0.25 |
| 10-30 06:51 | +10 stop | BTC | DOWN | 0.51 | 0.61 | 0.65 |
| 10-30 06:51 | +15 | BTC | DOWN | 0.51 | open |  |
| 10-30 06:51 | +10 | BTC | DOWN | 0.51 | 0.61 | 0.65 |
| 10-30 06:51 | +5 | BTC | DOWN | 0.51 | 0.61 | 0.65 |
| 10-30 06:51 | +10 stop | XRP | DOWN | 0.43 | 0.54 | 0.74 |
| 10-30 06:51 | +10 stop | SOL | UP | 0.60 | 0.74 | 1.09 |
| 10-30 06:51 | +10 stop | ETH | UP | 0.54 | 0.68 | 1.06 |
| 10-30 06:51 | +15 | ETH | UP | 0.54 | 0.72 | 1.47 |
| 10-30 06:51 | +10 | ETH | UP | 0.55 | 0.68 | 0.96 |
| 10-30 06:51 | +5 | ETH | UP | 0.55 | 0.68 | 0.96 |
| 10-30 06:51 | +10 stop | HYPE | DOWN | 0.65 | 0.42 | -2.64 |
| 10-30 06:51 | +20 | HYPE | DOWN | 0.65 | open |  |
| 10-30 06:51 | +15 | HYPE | DOWN | 0.65 | open |  |
| 10-30 06:51 | +10 | HYPE | DOWN | 0.65 | open |  |
| 10-30 06:51 | +5 | HYPE | DOWN | 0.65 | open |  |
| 10-30 06:50 | +10 stop | ZEC | DOWN | 0.62 | 0.39 | -2.63 |
| 10-30 06:50 | +20 | SOL | DOWN | 0.69 | open |  |
| 10-30 06:50 | +15 | SOL | DOWN | 0.69 | open |  |
| 10-30 06:50 | +10 | SOL | DOWN | 0.69 | open |  |
| 10-30 06:50 | +5 | SOL | DOWN | 0.68 | open |  |
| 10-30 06:50 | +10 stop | XRP | DOWN | 0.70 | 0.52 | -2.15 |
| 10-30 06:50 | +20 | XRP | DOWN | 0.70 | open |  |
| 10-30 06:50 | +15 | XRP | DOWN | 0.71 | open |  |
