# Range-Scalp Bot

*Updated Thu Nov 05 13:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48331 | 42109 | 6222 (73) | 3 | $-13772.69 | -4.5% |
| **+10¢** | 36085 | 28857 | 7228 (99) | 4 | $-12622.33 | -5.6% |
| **+15¢** | 30238 | 22455 | 7783 (127) | 6 | $-11513.61 | -6.1% |
| **+20¢** | 26862 | 18709 | 8153 (166) | 7 | $-10157.79 | -6.0% |
| **+10¢ (15¢ stop)** | 58908 | 58815 | 93 (56) | 2 | $-21865.56 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 13:38 | +10 stop | NEAR | UP | 0.54 | open |  |
| 11-05 13:38 | +10 stop | BTC | DOWN | 0.54 | open |  |
| 11-05 13:37 | +10 stop | SOL | DOWN | 0.51 | 0.72 | 1.77 |
| 11-05 13:37 | +10 stop | ETH | DOWN | 0.56 | 0.66 | 0.66 |
| 11-05 13:36 | +5 | SOL | DOWN | 0.57 | 0.72 | 1.17 |
| 11-05 13:36 | +5 | XRP | DOWN | 0.65 | 0.73 | 0.50 |
| 11-05 13:36 | +10 stop | BTC | UP | 0.61 | 0.45 | -1.95 |
| 11-05 13:36 | +5 | SOL | DOWN | 0.52 | 0.60 | 0.45 |
| 11-05 13:36 | +10 stop | HYPE | DOWN | 0.64 | 0.80 | 1.31 |
| 11-05 13:36 | +20 | HYPE | DOWN | 0.64 | 0.91 | 2.49 |
| 11-05 13:36 | +15 | HYPE | DOWN | 0.64 | 0.80 | 1.31 |
| 11-05 13:36 | +10 | HYPE | DOWN | 0.64 | 0.80 | 1.31 |
| 11-05 13:36 | +5 | HYPE | DOWN | 0.64 | 0.73 | 0.59 |
| 11-05 13:36 | +5 | XRP | DOWN | 0.60 | 0.66 | 0.27 |
| 11-05 13:35 | +10 stop | DOGE | UP | 0.61 | 0.74 | 0.99 |
| 11-05 13:35 | +10 stop | NEAR | UP | 0.64 | 0.79 | 1.21 |
| 11-05 13:34 | +10 stop | BNB | DOWN | 0.69 | 0.45 | -2.73 |
| 11-05 13:34 | +20 | BNB | DOWN | 0.69 | open |  |
| 11-05 13:34 | +15 | BNB | DOWN | 0.69 | open |  |
| 11-05 13:34 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-05 13:34 | +5 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-05 13:33 | +10 stop | BTC | DOWN | 0.55 | 0.40 | -1.85 |
| 11-05 13:33 | +10 stop | SOL | DOWN | 0.70 | 0.53 | -2.03 |
| 11-05 13:33 | +20 | SOL | DOWN | 0.70 | open |  |
| 11-05 13:33 | +15 | SOL | DOWN | 0.70 | open |  |
| 11-05 13:33 | +10 | SOL | DOWN | 0.70 | open |  |
| 11-05 13:33 | +5 | SOL | DOWN | 0.70 | 0.77 | 0.42 |
| 11-05 13:33 | +10 stop | ETH | DOWN | 0.67 | 0.51 | -1.94 |
| 11-05 13:33 | +20 | ETH | DOWN | 0.67 | open |  |
| 11-05 13:33 | +15 | ETH | DOWN | 0.67 | open |  |
| 11-05 13:33 | +10 | ETH | DOWN | 0.67 | 0.79 | 0.92 |
| 11-05 13:33 | +5 | ETH | DOWN | 0.67 | 0.74 | 0.40 |
| 11-05 13:32 | +10 stop | XRP | DOWN | 0.67 | 0.86 | 1.65 |
| 11-05 13:32 | +20 | XRP | DOWN | 0.67 | open |  |
| 11-05 13:32 | +15 | XRP | DOWN | 0.67 | 0.86 | 1.65 |
| 11-05 13:32 | +10 | XRP | DOWN | 0.66 | 0.86 | 1.75 |
| 11-05 13:32 | +5 | XRP | DOWN | 0.66 | 0.72 | 0.29 |
| 11-05 13:32 | +10 stop | DOGE | DOWN | 0.59 | 0.37 | -2.54 |
| 11-05 13:32 | +20 | DOGE | DOWN | 0.59 | open |  |
| 11-05 13:32 | +15 | DOGE | DOWN | 0.59 | open |  |
