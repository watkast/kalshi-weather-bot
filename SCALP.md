# Range-Scalp Bot

*Updated Wed Nov 18 00:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63341 | 55247 | 8094 (118) | 2 | $-17282.94 | -4.3% |
| **+10¢** | 47314 | 37843 | 9471 (159) | 3 | $-16180.75 | -5.4% |
| **+15¢** | 39666 | 29452 | 10214 (203) | 6 | $-14674.70 | -5.9% |
| **+20¢** | 35342 | 24624 | 10718 (258) | 6 | $-12913.96 | -5.8% |
| **+10¢ (15¢ stop)** | 77080 | 76922 | 158 (93) | 3 | $-28396.45 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 00:34 | +10 stop | ETH | UP | 0.63 | 0.74 | 0.79 |
| 11-18 00:34 | +20 | ETH | UP | 0.63 | open |  |
| 11-18 00:34 | +15 | ETH | UP | 0.63 | open |  |
| 11-18 00:34 | +10 | ETH | UP | 0.63 | 0.74 | 0.79 |
| 11-18 00:34 | +5 | ETH | UP | 0.63 | 0.74 | 0.79 |
| 11-18 00:34 | +10 stop | BTC | UP | 0.65 | 0.75 | 0.70 |
| 11-18 00:34 | +20 | BTC | UP | 0.65 | open |  |
| 11-18 00:34 | +15 | BTC | UP | 0.65 | open |  |
| 11-18 00:34 | +10 | BTC | UP | 0.65 | 0.75 | 0.70 |
| 11-18 00:34 | +5 | BTC | UP | 0.65 | 0.75 | 0.70 |
| 11-18 00:34 | +10 stop | DOGE | DOWN | 0.60 | open |  |
| 11-18 00:33 | +5 | XRP | UP | 0.64 | 0.75 | 0.79 |
| 11-18 00:33 | +10 stop | HYPE | UP | 0.54 | open |  |
| 11-18 00:33 | +5 | XRP | UP | 0.62 | 0.68 | 0.27 |
| 11-18 00:33 | +10 stop | SOL | UP | 0.54 | open |  |
| 11-18 00:33 | +20 | SOL | UP | 0.54 | open |  |
| 11-18 00:33 | +15 | SOL | UP | 0.54 | open |  |
| 11-18 00:33 | +10 | SOL | UP | 0.55 | open |  |
| 11-18 00:33 | +5 | SOL | UP | 0.55 | 0.60 | 0.15 |
| 11-18 00:33 | +10 stop | XRP | UP | 0.64 | 0.75 | 0.79 |
| 11-18 00:33 | +20 | XRP | UP | 0.64 | open |  |
| 11-18 00:33 | +15 | XRP | UP | 0.65 | open |  |
| 11-18 00:33 | +10 | XRP | UP | 0.62 | 0.75 | 0.99 |
| 11-18 00:33 | +5 | XRP | UP | 0.64 | 0.69 | 0.18 |
| 11-18 00:32 | +5 | HYPE | UP | 0.63 | open |  |
| 11-18 00:32 | +10 stop | DOGE | UP | 0.64 | 0.45 | -2.25 |
| 11-18 00:32 | +20 | DOGE | UP | 0.64 | open |  |
| 11-18 00:32 | +15 | DOGE | UP | 0.63 | open |  |
| 11-18 00:32 | +10 | DOGE | UP | 0.63 | open |  |
| 11-18 00:32 | +5 | DOGE | UP | 0.64 | open |  |
| 11-18 00:30 | +10 stop | HYPE | UP | 0.68 | 0.52 | -1.94 |
| 11-18 00:30 | +20 | HYPE | UP | 0.68 | open |  |
| 11-18 00:30 | +15 | HYPE | UP | 0.68 | open |  |
| 11-18 00:30 | +10 | HYPE | UP | 0.68 | open |  |
| 11-18 00:30 | +5 | HYPE | UP | 0.68 | 0.75 | 0.40 |
| 11-18 00:26 | +10 stop | DOGE | DOWN | 0.56 | 0.74 | 1.48 |
| 11-18 00:26 | +10 stop | HYPE | DOWN | 0.69 | 0.95 | 2.38 |
| 11-18 00:26 | +10 stop | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 11-18 00:26 | +10 | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 11-18 00:26 | +5 | BNB | DOWN | 0.71 | 0.82 | 0.84 |
