# Range-Scalp Bot

*Updated Thu Nov 19 00:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64501 | 56267 | 8234 (124) | 4 | $-17530.06 | -4.3% |
| **+10¢** | 48185 | 38555 | 9630 (165) | 4 | $-16341.77 | -5.4% |
| **+15¢** | 40405 | 30024 | 10381 (210) | 4 | $-14761.21 | -5.8% |
| **+20¢** | 35979 | 25081 | 10898 (265) | 6 | $-13056.96 | -5.8% |
| **+10¢ (15¢ stop)** | 78466 | 78302 | 164 (98) | 4 | $-28854.16 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 00:35 | +10 | XRP | UP | 0.67 | open |  |
| 11-19 00:35 | +5 | XRP | UP | 0.66 | open |  |
| 11-19 00:35 | +10 stop | XRP | UP | 0.71 | open |  |
| 11-19 00:34 | +10 stop | SOL | UP | 0.59 | 0.73 | 1.09 |
| 11-19 00:34 | +10 | SOL | UP | 0.61 | 0.73 | 0.89 |
| 11-19 00:34 | +5 | XRP | UP | 0.62 | 0.68 | 0.27 |
| 11-19 00:34 | +10 stop | ETH | UP | 0.55 | open |  |
| 11-19 00:34 | +20 | ETH | UP | 0.53 | open |  |
| 11-19 00:34 | +15 | ETH | UP | 0.56 | open |  |
| 11-19 00:34 | +10 | ETH | UP | 0.56 | open |  |
| 11-19 00:34 | +5 | ETH | UP | 0.56 | open |  |
| 11-19 00:34 | +5 | SOL | UP | 0.66 | 0.73 | 0.40 |
| 11-19 00:34 | +10 stop | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 11-19 00:34 | +10 stop | HYPE | UP | 0.70 | open |  |
| 11-19 00:34 | +5 | HYPE | UP | 0.70 | 0.75 | 0.21 |
| 11-19 00:33 | +10 stop | DOGE | UP | 0.68 | open |  |
| 11-19 00:33 | +15 | DOGE | UP | 0.68 | open |  |
| 11-19 00:33 | +10 | DOGE | UP | 0.68 | open |  |
| 11-19 00:33 | +10 stop | SOL | UP | 0.52 | 0.62 | 0.65 |
| 11-19 00:33 | +20 | SOL | UP | 0.52 | 0.73 | 1.78 |
| 11-19 00:33 | +15 | SOL | UP | 0.52 | 0.68 | 1.26 |
| 11-19 00:33 | +10 | SOL | UP | 0.52 | 0.62 | 0.65 |
| 11-19 00:33 | +5 | SOL | UP | 0.52 | 0.61 | 0.55 |
| 11-19 00:33 | +10 stop | XRP | UP | 0.55 | 0.68 | 0.96 |
| 11-19 00:33 | +5 | XRP | UP | 0.55 | 0.62 | 0.35 |
| 11-19 00:33 | +10 stop | ETH | DOWN | 0.41 | 0.62 | 1.76 |
| 11-19 00:33 | +20 | ETH | DOWN | 0.41 | 0.62 | 1.76 |
| 11-19 00:33 | +15 | ETH | DOWN | 0.41 | 0.62 | 1.76 |
| 11-19 00:33 | +10 | ETH | DOWN | 0.41 | 0.62 | 1.76 |
| 11-19 00:33 | +5 | ETH | DOWN | 0.41 | 0.62 | 1.76 |
| 11-19 00:33 | +10 stop | SOL | DOWN | 0.39 | 0.62 | 1.96 |
| 11-19 00:33 | +20 | SOL | DOWN | 0.39 | 0.62 | 1.96 |
| 11-19 00:33 | +15 | SOL | DOWN | 0.39 | 0.62 | 1.96 |
| 11-19 00:33 | +10 | SOL | DOWN | 0.39 | 0.62 | 1.96 |
| 11-19 00:33 | +5 | SOL | DOWN | 0.39 | 0.62 | 1.96 |
| 11-19 00:33 | +10 stop | XRP | DOWN | 0.39 | 0.54 | 1.15 |
| 11-19 00:33 | +5 | XRP | DOWN | 0.39 | 0.54 | 1.15 |
| 11-19 00:32 | +10 stop | NEAR | UP | 0.65 | 0.77 | 0.91 |
| 11-19 00:32 | +20 | NEAR | UP | 0.65 | 0.85 | 1.75 |
| 11-19 00:32 | +15 | NEAR | UP | 0.65 | 0.81 | 1.33 |
