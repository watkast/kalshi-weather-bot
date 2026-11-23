# Range-Scalp Bot

*Updated Mon Nov 23 11:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69896 | 60995 | 8901 (146) | 2 | $-18790.60 | -4.3% |
| **+10¢** | 52155 | 41753 | 10402 (189) | 1 | $-17493.59 | -5.3% |
| **+15¢** | 43708 | 32503 | 11205 (245) | 1 | $-15610.81 | -5.7% |
| **+20¢** | 38920 | 27129 | 11791 (310) | 1 | $-13964.73 | -5.7% |
| **+10¢ (15¢ stop)** | 85118 | 84928 | 190 (118) | 1 | $-31256.51 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 11:42 | +10 stop | HYPE | DOWN | 0.63 | open |  |
| 11-23 11:42 | +20 | HYPE | DOWN | 0.63 | open |  |
| 11-23 11:42 | +15 | HYPE | DOWN | 0.63 | open |  |
| 11-23 11:42 | +10 | HYPE | DOWN | 0.63 | open |  |
| 11-23 11:42 | +5 | HYPE | DOWN | 0.63 | open |  |
| 11-23 11:39 | +10 stop | NEAR | DOWN | 0.69 | 0.84 | 1.25 |
| 11-23 11:39 | +20 | NEAR | DOWN | 0.69 | 0.93 | 2.23 |
| 11-23 11:39 | +15 | NEAR | DOWN | 0.69 | 0.84 | 1.25 |
| 11-23 11:39 | +10 | NEAR | DOWN | 0.69 | 0.84 | 1.25 |
| 11-23 11:39 | +5 | NEAR | DOWN | 0.70 | 0.84 | 1.19 |
| 11-23 11:36 | +10 stop | XRP | UP | 0.59 | 0.71 | 0.88 |
| 11-23 11:36 | +15 | XRP | UP | 0.59 | 0.75 | 1.29 |
| 11-23 11:36 | +10 | XRP | UP | 0.59 | 0.71 | 0.88 |
| 11-23 11:36 | +10 stop | BNB | UP | 0.70 | 0.85 | 1.26 |
| 11-23 11:36 | +15 | BNB | UP | 0.70 | 0.85 | 1.26 |
| 11-23 11:36 | +10 | BNB | UP | 0.70 | 0.85 | 1.26 |
| 11-23 11:36 | +5 | BNB | UP | 0.70 | 0.85 | 1.26 |
| 11-23 11:36 | +5 | SOL | UP | 0.59 | 0.67 | 0.48 |
| 11-23 11:34 | +10 stop | XRP | UP | 0.59 | 0.69 | 0.68 |
| 11-23 11:34 | +10 stop | SOL | UP | 0.66 | 0.77 | 0.83 |
| 11-23 11:34 | +5 | ZEC | UP | 0.69 | 0.76 | 0.42 |
| 11-23 11:33 | +5 | ZEC | UP | 0.58 | 0.64 | 0.25 |
| 11-23 11:33 | +5 | HYPE | UP | 0.69 | 0.76 | 0.42 |
| 11-23 11:33 | +15 | ZEC | UP | 0.66 | 0.88 | 1.96 |
| 11-23 11:32 | +10 stop | ZEC | UP | 0.65 | 0.76 | 0.81 |
| 11-23 11:32 | +10 | ZEC | UP | 0.65 | 0.76 | 0.81 |
| 11-23 11:32 | +5 | ZEC | UP | 0.60 | 0.65 | 0.17 |
| 11-23 11:32 | +5 | NEAR | DOWN | 0.69 | 0.75 | 0.31 |
| 11-23 11:32 | +10 stop | HYPE | UP | 0.60 | 0.73 | 0.99 |
| 11-23 11:32 | +20 | HYPE | UP | 0.60 | 0.89 | 2.66 |
| 11-23 11:32 | +15 | HYPE | UP | 0.60 | 0.76 | 1.30 |
| 11-23 11:32 | +10 | HYPE | UP | 0.60 | 0.73 | 0.99 |
| 11-23 11:32 | +5 | HYPE | UP | 0.60 | 0.65 | 0.17 |
| 11-23 11:32 | +10 stop | DOGE | DOWN | 0.44 | 0.23 | -2.41 |
| 11-23 11:32 | +10 stop | SOL | UP | 0.66 | 0.49 | -2.04 |
| 11-23 11:31 | +10 stop | BNB | UP | 0.66 | 0.77 | 0.81 |
| 11-23 11:31 | +20 | BNB | UP | 0.66 | 0.91 | 2.27 |
| 11-23 11:31 | +15 | BNB | UP | 0.66 | 0.81 | 1.23 |
| 11-23 11:31 | +10 | BNB | UP | 0.66 | 0.77 | 0.81 |
| 11-23 11:31 | +5 | BNB | UP | 0.66 | 0.73 | 0.40 |
