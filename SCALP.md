# Range-Scalp Bot

*Updated Mon Nov 23 13:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70006 | 61092 | 8914 (146) | 4 | $-18818.21 | -4.3% |
| **+10¢** | 52229 | 41816 | 10413 (189) | 6 | $-17490.49 | -5.3% |
| **+15¢** | 43766 | 32551 | 11215 (245) | 6 | $-15588.78 | -5.7% |
| **+20¢** | 38973 | 27171 | 11802 (310) | 6 | $-13944.48 | -5.7% |
| **+10¢ (15¢ stop)** | 85275 | 85085 | 190 (118) | 3 | $-31341.59 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 13:04 | +10 stop | ETH | UP | 0.60 | open |  |
| 11-23 13:04 | +10 stop | DOGE | UP | 0.59 | open |  |
| 11-23 13:03 | +10 stop | XRP | UP | 0.62 | 0.75 | 0.99 |
| 11-23 13:03 | +10 | XRP | UP | 0.62 | 0.75 | 0.99 |
| 11-23 13:03 | +5 | XRP | UP | 0.65 | 0.70 | 0.19 |
| 11-23 13:03 | +10 stop | BNB | DOWN | 0.63 | 0.43 | -2.40 |
| 11-23 13:02 | +10 stop | ETH | DOWN | 0.58 | 0.41 | -2.05 |
| 11-23 13:02 | +10 stop | BTC | DOWN | 0.63 | open |  |
| 11-23 13:02 | +10 stop | SOL | DOWN | 0.63 | 0.47 | -1.95 |
| 11-23 13:02 | +5 | SOL | DOWN | 0.63 | open |  |
| 11-23 13:02 | +10 stop | XRP | UP | 0.51 | 0.62 | 0.75 |
| 11-23 13:02 | +20 | XRP | UP | 0.51 | 0.75 | 2.08 |
| 11-23 13:02 | +15 | XRP | UP | 0.51 | 0.70 | 1.57 |
| 11-23 13:02 | +10 | XRP | UP | 0.51 | 0.62 | 0.75 |
| 11-23 13:02 | +5 | XRP | UP | 0.51 | 0.57 | 0.24 |
| 11-23 13:02 | +5 | ZEC | DOWN | 0.61 | open |  |
| 11-23 13:01 | +5 | BTC | UP | 0.51 | open |  |
| 11-23 13:01 | +10 stop | HYPE | DOWN | 0.58 | 0.42 | -1.96 |
| 11-23 13:01 | +20 | HYPE | DOWN | 0.58 | open |  |
| 11-23 13:01 | +15 | HYPE | DOWN | 0.58 | open |  |
| 11-23 13:01 | +10 | HYPE | DOWN | 0.58 | open |  |
| 11-23 13:01 | +5 | HYPE | DOWN | 0.59 | 0.65 | 0.27 |
| 11-23 13:01 | +10 stop | ZEC | UP | 0.52 | 0.62 | 0.65 |
| 11-23 13:01 | +20 | ZEC | UP | 0.51 | 0.71 | 1.67 |
| 11-23 13:01 | +15 | ZEC | UP | 0.51 | 0.71 | 1.67 |
| 11-23 13:01 | +10 | ZEC | UP | 0.51 | 0.62 | 0.75 |
| 11-23 13:01 | +5 | ZEC | UP | 0.51 | 0.56 | 0.14 |
| 11-23 13:01 | +10 stop | DOGE | UP | 0.60 | 0.41 | -2.24 |
| 11-23 13:01 | +20 | DOGE | UP | 0.60 | open |  |
| 11-23 13:01 | +15 | DOGE | UP | 0.60 | open |  |
| 11-23 13:01 | +10 | DOGE | UP | 0.59 | open |  |
| 11-23 13:01 | +5 | DOGE | UP | 0.59 | 0.65 | 0.25 |
| 11-23 13:01 | +10 stop | BNB | UP | 0.54 | 0.34 | -2.34 |
| 11-23 13:01 | +20 | BNB | UP | 0.53 | open |  |
| 11-23 13:01 | +15 | BNB | UP | 0.53 | open |  |
| 11-23 13:01 | +10 | BNB | UP | 0.53 | open |  |
| 11-23 13:01 | +5 | BNB | UP | 0.53 | open |  |
| 11-23 13:01 | +10 stop | ETH | UP | 0.55 | 0.39 | -1.95 |
| 11-23 13:01 | +20 | ETH | UP | 0.55 | open |  |
| 11-23 13:01 | +15 | ETH | UP | 0.55 | open |  |
