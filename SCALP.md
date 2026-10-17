# Range-Scalp Bot

*Updated Sat Oct 17 03:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20311 | 17665 | 2646 (29) | 3 | $-6023.01 | -4.7% |
| **+10¢** | 15304 | 12251 | 3053 (41) | 4 | $-5375.15 | -5.6% |
| **+15¢** | 12794 | 9511 | 3283 (60) | 4 | $-4848.31 | -6.0% |
| **+20¢** | 11344 | 7905 | 3439 (79) | 5 | $-4291.60 | -6.0% |
| **+10¢ (15¢ stop)** | 24974 | 24924 | 50 (29) | 2 | $-9469.02 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 03:38 | +5 | ETH | DOWN | 0.68 | open |  |
| 10-17 03:38 | +10 stop | ETH | DOWN | 0.64 | open |  |
| 10-17 03:37 | +20 | SOL | UP | 0.60 | open |  |
| 10-17 03:37 | +15 | SOL | UP | 0.60 | 0.76 | 1.30 |
| 10-17 03:37 | +5 | SOL | UP | 0.60 | 0.69 | 0.58 |
| 10-17 03:36 | +10 stop | SOL | UP | 0.67 | open |  |
| 10-17 03:36 | +10 | SOL | UP | 0.67 | open |  |
| 10-17 03:36 | +5 | SOL | UP | 0.67 | 0.75 | 0.50 |
| 10-17 03:36 | +10 stop | HYPE | UP | 0.67 | 0.52 | -1.84 |
| 10-17 03:36 | +10 stop | ETH | UP | 0.50 | 0.60 | 0.65 |
| 10-17 03:35 | +10 stop | SOL | DOWN | 0.50 | 0.31 | -2.23 |
| 10-17 03:35 | +10 stop | BTC | DOWN | 0.46 | 0.56 | 0.64 |
| 10-17 03:35 | +10 stop | BNB | UP | 0.69 | 0.82 | 1.04 |
| 10-17 03:35 | +20 | BNB | UP | 0.69 | open |  |
| 10-17 03:35 | +15 | BNB | UP | 0.69 | open |  |
| 10-17 03:35 | +10 | BNB | UP | 0.69 | 0.82 | 1.04 |
| 10-17 03:35 | +5 | BNB | UP | 0.69 | 0.74 | 0.21 |
| 10-17 03:34 | +10 stop | HYPE | UP | 0.52 | 0.62 | 0.65 |
| 10-17 03:34 | +10 stop | SOL | UP | 0.55 | 0.38 | -2.05 |
| 10-17 03:34 | +20 | SOL | UP | 0.55 | 0.75 | 1.68 |
| 10-17 03:34 | +15 | SOL | UP | 0.55 | 0.75 | 1.68 |
| 10-17 03:34 | +10 | SOL | UP | 0.55 | 0.68 | 0.96 |
| 10-17 03:34 | +5 | SOL | UP | 0.55 | 0.68 | 0.96 |
| 10-17 03:33 | +10 stop | BTC | UP | 0.65 | 0.47 | -2.14 |
| 10-17 03:33 | +15 | BTC | UP | 0.65 | open |  |
| 10-17 03:33 | +10 | BTC | UP | 0.65 | open |  |
| 10-17 03:33 | +5 | BTC | UP | 0.65 | open |  |
| 10-17 03:32 | +10 stop | HYPE | UP | 0.67 | 0.52 | -1.84 |
| 10-17 03:32 | +20 | HYPE | UP | 0.67 | open |  |
| 10-17 03:32 | +15 | HYPE | UP | 0.66 | open |  |
| 10-17 03:32 | +10 | HYPE | UP | 0.66 | open |  |
| 10-17 03:32 | +5 | HYPE | UP | 0.66 | open |  |
| 10-17 03:32 | +5 | SOL | UP | 0.67 | 0.76 | 0.61 |
| 10-17 03:32 | +10 stop | ETH | UP | 0.59 | 0.70 | 0.78 |
| 10-17 03:32 | +10 stop | BNB | UP | 0.59 | 0.74 | 1.19 |
| 10-17 03:32 | +20 | BNB | UP | 0.59 | 0.80 | 1.81 |
| 10-17 03:32 | +15 | BNB | UP | 0.59 | 0.74 | 1.19 |
| 10-17 03:32 | +10 | BNB | UP | 0.59 | 0.74 | 1.19 |
| 10-17 03:32 | +5 | BNB | UP | 0.59 | 0.74 | 1.19 |
| 10-17 03:32 | +10 stop | BTC | UP | 0.62 | 0.77 | 1.20 |
