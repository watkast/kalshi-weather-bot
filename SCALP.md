# Range-Scalp Bot

*Updated Thu Nov 19 06:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64892 | 56632 | 8260 (124) | 3 | $-17477.16 | -4.3% |
| **+10¢** | 48473 | 38812 | 9661 (165) | 5 | $-16256.68 | -5.3% |
| **+15¢** | 40650 | 30231 | 10419 (210) | 5 | $-14662.02 | -5.7% |
| **+20¢** | 36199 | 25258 | 10941 (265) | 5 | $-12960.64 | -5.7% |
| **+10¢ (15¢ stop)** | 78951 | 78787 | 164 (98) | 1 | $-28988.16 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 06:39 | +5 | ETH | DOWN | 0.56 | 0.61 | 0.15 |
| 11-19 06:39 | +10 stop | ETH | DOWN | 0.62 | 0.41 | -2.44 |
| 11-19 06:39 | +10 stop | SOL | UP | 0.53 | open |  |
| 11-19 06:37 | +10 stop | ETH | UP | 0.61 | 0.43 | -2.15 |
| 11-19 06:36 | +10 stop | SOL | UP | 0.68 | 0.53 | -1.84 |
| 11-19 06:36 | +10 stop | HYPE | UP | 0.66 | 0.83 | 1.44 |
| 11-19 06:36 | +20 | HYPE | UP | 0.66 | 0.88 | 1.96 |
| 11-19 06:36 | +15 | HYPE | UP | 0.66 | 0.83 | 1.44 |
| 11-19 06:36 | +10 | HYPE | UP | 0.66 | 0.83 | 1.44 |
| 11-19 06:36 | +5 | HYPE | UP | 0.66 | 0.75 | 0.60 |
| 11-19 06:32 | +10 stop | BTC | UP | 0.71 | 0.50 | -2.43 |
| 11-19 06:31 | +10 stop | SOL | UP | 0.70 | 0.82 | 0.94 |
| 11-19 06:31 | +10 stop | NEAR | DOWN | 0.54 | 0.29 | -2.83 |
| 11-19 06:31 | +20 | NEAR | DOWN | 0.54 | open |  |
| 11-19 06:31 | +15 | NEAR | DOWN | 0.54 | open |  |
| 11-19 06:31 | +10 | NEAR | DOWN | 0.54 | open |  |
| 11-19 06:31 | +5 | NEAR | DOWN | 0.54 | 0.60 | 0.25 |
| 11-19 06:30 | +10 stop | ETH | DOWN | 0.56 | 0.29 | -3.03 |
| 11-19 06:30 | +20 | ETH | DOWN | 0.56 | open |  |
| 11-19 06:30 | +15 | ETH | DOWN | 0.56 | open |  |
| 11-19 06:30 | +10 | ETH | DOWN | 0.56 | open |  |
| 11-19 06:30 | +5 | ETH | DOWN | 0.55 | 0.62 | 0.35 |
| 11-19 06:30 | +10 stop | SOL | DOWN | 0.53 | 0.30 | -2.63 |
| 11-19 06:30 | +20 | SOL | DOWN | 0.53 | open |  |
| 11-19 06:30 | +15 | SOL | DOWN | 0.53 | open |  |
| 11-19 06:30 | +10 | SOL | DOWN | 0.53 | open |  |
| 11-19 06:30 | +5 | SOL | DOWN | 0.53 | open |  |
| 11-19 06:30 | +10 stop | BTC | DOWN | 0.55 | 0.37 | -2.15 |
| 11-19 06:30 | +20 | BTC | DOWN | 0.55 | open |  |
| 11-19 06:30 | +15 | BTC | DOWN | 0.55 | open |  |
| 11-19 06:30 | +10 | BTC | DOWN | 0.55 | open |  |
| 11-19 06:30 | +5 | BTC | DOWN | 0.55 | open |  |
| 11-19 06:30 | +10 stop | XRP | DOWN | 0.50 | 0.32 | -2.14 |
| 11-19 06:30 | +20 | XRP | DOWN | 0.51 | open |  |
| 11-19 06:30 | +15 | XRP | DOWN | 0.51 | open |  |
| 11-19 06:30 | +10 | XRP | DOWN | 0.51 | open |  |
| 11-19 06:30 | +5 | XRP | DOWN | 0.51 | open |  |
| 11-19 06:30 | +10 stop | HYPE | UP | 0.61 | 0.71 | 0.68 |
| 11-19 06:30 | +20 | HYPE | UP | 0.61 | 0.81 | 1.72 |
| 11-19 06:30 | +15 | HYPE | UP | 0.61 | 0.81 | 1.72 |
