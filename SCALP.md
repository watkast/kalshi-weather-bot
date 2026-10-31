# Range-Scalp Bot

*Updated Sat Oct 31 15:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42416 | 36998 | 5418 (59) | 1 | $-11925.49 | -4.5% |
| **+10¢** | 31624 | 25352 | 6272 (81) | 1 | $-10720.55 | -5.4% |
| **+15¢** | 26450 | 19687 | 6763 (109) | 1 | $-9816.73 | -5.9% |
| **+20¢** | 23491 | 16403 | 7088 (141) | 1 | $-8681.69 | -5.9% |
| **+10¢ (15¢ stop)** | 51723 | 51644 | 79 (44) | 1 | $-19540.71 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 15:37 | +10 stop | BNB | DOWN | 0.65 | open |  |
| 10-31 15:37 | +10 | BNB | DOWN | 0.65 | open |  |
| 10-31 15:37 | +5 | BNB | DOWN | 0.67 | open |  |
| 10-31 15:35 | +5 | SOL | UP | 0.67 | 0.73 | 0.30 |
| 10-31 15:35 | +10 stop | SOL | UP | 0.67 | 0.77 | 0.71 |
| 10-31 15:33 | +5 | NEAR | UP | 0.65 | 0.72 | 0.39 |
| 10-31 15:33 | +10 stop | SOL | DOWN | 0.62 | 0.42 | -2.35 |
| 10-31 15:32 | +5 | DOGE | UP | 0.61 | 0.72 | 0.79 |
| 10-31 15:31 | +10 stop | HYPE | UP | 0.65 | 0.79 | 1.12 |
| 10-31 15:31 | +20 | HYPE | UP | 0.64 | 0.86 | 1.90 |
| 10-31 15:31 | +15 | HYPE | UP | 0.64 | 0.81 | 1.38 |
| 10-31 15:31 | +10 | HYPE | UP | 0.65 | 0.79 | 1.12 |
| 10-31 15:31 | +5 | HYPE | UP | 0.65 | 0.79 | 1.12 |
| 10-31 15:31 | +10 stop | NEAR | UP | 0.61 | 0.72 | 0.78 |
| 10-31 15:31 | +20 | NEAR | UP | 0.61 | 0.83 | 1.93 |
| 10-31 15:31 | +15 | NEAR | UP | 0.61 | 0.76 | 1.20 |
| 10-31 15:31 | +10 | NEAR | UP | 0.61 | 0.72 | 0.78 |
| 10-31 15:31 | +5 | NEAR | UP | 0.61 | 0.66 | 0.17 |
| 10-31 15:31 | +10 stop | BTC | UP | 0.62 | 0.75 | 0.99 |
| 10-31 15:31 | +20 | BTC | UP | 0.61 | 0.83 | 1.93 |
| 10-31 15:31 | +15 | BTC | UP | 0.61 | 0.83 | 1.93 |
| 10-31 15:31 | +10 | BTC | UP | 0.62 | 0.75 | 0.99 |
| 10-31 15:31 | +5 | BTC | UP | 0.62 | 0.75 | 0.99 |
| 10-31 15:31 | +10 stop | DOGE | UP | 0.63 | 0.74 | 0.79 |
| 10-31 15:31 | +20 | DOGE | UP | 0.63 | 0.86 | 2.04 |
| 10-31 15:31 | +15 | DOGE | UP | 0.63 | 0.78 | 1.20 |
| 10-31 15:31 | +10 | DOGE | UP | 0.63 | 0.74 | 0.79 |
| 10-31 15:31 | +5 | DOGE | UP | 0.63 | 0.68 | 0.17 |
| 10-31 15:31 | +10 stop | SOL | UP | 0.59 | 0.40 | -2.24 |
| 10-31 15:31 | +20 | SOL | UP | 0.59 | 0.83 | 2.13 |
| 10-31 15:31 | +15 | SOL | UP | 0.59 | 0.77 | 1.50 |
| 10-31 15:31 | +10 | SOL | UP | 0.59 | 0.70 | 0.78 |
| 10-31 15:31 | +5 | SOL | UP | 0.59 | 0.64 | 0.16 |
| 10-31 15:31 | +10 stop | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 10-31 15:31 | +20 | BNB | DOWN | 0.68 | open |  |
| 10-31 15:31 | +15 | BNB | DOWN | 0.68 | open |  |
| 10-31 15:31 | +10 | BNB | DOWN | 0.68 | 0.81 | 1.03 |
| 10-31 15:31 | +5 | BNB | DOWN | 0.68 | 0.77 | 0.57 |
| 10-31 15:25 | +10 stop | ETH | DOWN | 0.69 | 0.54 | -1.83 |
| 10-31 15:25 | +20 | ETH | DOWN | 0.69 | yes | -7.05 |
