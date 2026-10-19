# Range-Scalp Bot

*Updated Mon Oct 19 02:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23344 | 20300 | 3044 (30) | 6 | $-6947.24 | -4.7% |
| **+10¢** | 17563 | 14054 | 3509 (44) | 6 | $-6186.50 | -5.6% |
| **+15¢** | 14720 | 10937 | 3783 (66) | 7 | $-5623.57 | -6.1% |
| **+20¢** | 13031 | 9074 | 3957 (84) | 7 | $-4999.38 | -6.1% |
| **+10¢ (15¢ stop)** | 28745 | 28694 | 51 (30) | 2 | $-10929.79 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 02:37 | +10 stop | NEAR | UP | 0.68 | open |  |
| 10-19 02:36 | +10 stop | SOL | UP | 0.71 | open |  |
| 10-19 02:35 | +5 | BTC | UP | 0.68 | 0.85 | 1.45 |
| 10-19 02:35 | +10 stop | BNB | UP | 0.68 | 0.84 | 1.34 |
| 10-19 02:35 | +10 stop | HYPE | UP | 0.60 | 0.73 | 0.99 |
| 10-19 02:35 | +10 stop | NEAR | DOWN | 0.60 | 0.41 | -2.23 |
| 10-19 02:34 | +10 stop | BNB | UP | 0.54 | 0.64 | 0.65 |
| 10-19 02:33 | +10 stop | XRP | UP | 0.61 | 0.73 | 0.89 |
| 10-19 02:33 | +10 stop | ETH | UP | 0.66 | 0.77 | 0.81 |
| 10-19 02:33 | +10 stop | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-19 02:33 | +20 | ZEC | DOWN | 0.67 | open |  |
| 10-19 02:33 | +15 | ZEC | DOWN | 0.67 | open |  |
| 10-19 02:33 | +10 | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-19 02:33 | +5 | ZEC | DOWN | 0.68 | 0.77 | 0.61 |
| 10-19 02:33 | +10 stop | SOL | UP | 0.65 | 0.42 | -2.64 |
| 10-19 02:33 | +10 stop | BTC | UP | 0.64 | 0.85 | 1.84 |
| 10-19 02:33 | +20 | BTC | UP | 0.64 | 0.85 | 1.84 |
| 10-19 02:33 | +15 | BTC | UP | 0.64 | 0.85 | 1.84 |
| 10-19 02:33 | +10 | BTC | UP | 0.64 | 0.85 | 1.84 |
| 10-19 02:33 | +5 | BTC | UP | 0.64 | 0.69 | 0.18 |
| 10-19 02:31 | +10 stop | HYPE | DOWN | 0.65 | 0.49 | -1.94 |
| 10-19 02:31 | +20 | HYPE | DOWN | 0.65 | open |  |
| 10-19 02:31 | +15 | HYPE | DOWN | 0.65 | open |  |
| 10-19 02:31 | +10 | HYPE | DOWN | 0.65 | open |  |
| 10-19 02:31 | +5 | HYPE | DOWN | 0.65 | open |  |
| 10-19 02:31 | +10 stop | XRP | DOWN | 0.62 | 0.45 | -2.05 |
| 10-19 02:31 | +20 | XRP | DOWN | 0.62 | open |  |
| 10-19 02:31 | +15 | XRP | DOWN | 0.62 | open |  |
| 10-19 02:31 | +10 | XRP | DOWN | 0.62 | open |  |
| 10-19 02:31 | +5 | XRP | DOWN | 0.62 | open |  |
| 10-19 02:31 | +10 stop | SOL | DOWN | 0.58 | 0.37 | -2.45 |
| 10-19 02:31 | +20 | SOL | DOWN | 0.58 | open |  |
| 10-19 02:31 | +15 | SOL | DOWN | 0.58 | open |  |
| 10-19 02:31 | +10 | SOL | DOWN | 0.58 | open |  |
| 10-19 02:31 | +5 | SOL | DOWN | 0.58 | open |  |
| 10-19 02:31 | +10 stop | ETH | DOWN | 0.61 | 0.40 | -2.44 |
| 10-19 02:31 | +20 | ETH | DOWN | 0.61 | open |  |
| 10-19 02:31 | +15 | ETH | DOWN | 0.61 | open |  |
| 10-19 02:31 | +10 | ETH | DOWN | 0.61 | open |  |
| 10-19 02:31 | +5 | ETH | DOWN | 0.61 | open |  |
