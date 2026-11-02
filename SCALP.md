# Range-Scalp Bot

*Updated Mon Nov 02 23:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45301 | 39443 | 5858 (67) | 3 | $-13108.37 | -4.6% |
| **+10¢** | 33813 | 27026 | 6787 (89) | 3 | $-11977.69 | -5.6% |
| **+15¢** | 28283 | 20979 | 7304 (116) | 3 | $-11036.44 | -6.2% |
| **+20¢** | 25120 | 17471 | 7649 (151) | 3 | $-9792.86 | -6.2% |
| **+10¢ (15¢ stop)** | 55269 | 55182 | 87 (51) | 0 | $-20871.45 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 23:42 | +10 stop | HYPE | DOWN | 0.61 | 0.46 | -1.85 |
| 11-02 23:41 | +10 stop | ZEC | UP | 0.69 | 0.81 | 0.95 |
| 11-02 23:41 | +10 stop | HYPE | DOWN | 0.71 | 0.53 | -2.13 |
| 11-02 23:41 | +20 | HYPE | DOWN | 0.71 | 0.92 | 1.93 |
| 11-02 23:41 | +15 | HYPE | DOWN | 0.71 | 0.92 | 1.93 |
| 11-02 23:41 | +10 | HYPE | DOWN | 0.71 | 0.92 | 1.93 |
| 11-02 23:41 | +5 | HYPE | DOWN | 0.71 | 0.92 | 1.93 |
| 11-02 23:39 | +10 stop | ZEC | UP | 0.69 | 0.81 | 0.94 |
| 11-02 23:37 | +10 stop | ZEC | DOWN | 0.55 | 0.40 | -1.85 |
| 11-02 23:35 | +10 stop | NEAR | UP | 0.59 | 0.70 | 0.78 |
| 11-02 23:33 | +10 stop | DOGE | UP | 0.60 | 0.71 | 0.78 |
| 11-02 23:33 | +10 stop | SOL | UP | 0.62 | 0.72 | 0.68 |
| 11-02 23:33 | +10 stop | BTC | UP | 0.71 | 0.84 | 1.05 |
| 11-02 23:33 | +20 | BTC | UP | 0.71 | 0.92 | 1.87 |
| 11-02 23:33 | +15 | BTC | UP | 0.71 | 0.89 | 1.58 |
| 11-02 23:33 | +10 | BTC | UP | 0.70 | 0.84 | 1.15 |
| 11-02 23:33 | +5 | BTC | UP | 0.70 | 0.76 | 0.32 |
| 11-02 23:33 | +10 stop | ZEC | UP | 0.58 | 0.69 | 0.77 |
| 11-02 23:31 | +10 stop | SOL | DOWN | 0.57 | 0.35 | -2.54 |
| 11-02 23:31 | +20 | SOL | DOWN | 0.57 | open |  |
| 11-02 23:31 | +15 | SOL | DOWN | 0.57 | open |  |
| 11-02 23:31 | +10 | SOL | DOWN | 0.57 | open |  |
| 11-02 23:31 | +5 | SOL | DOWN | 0.57 | open |  |
| 11-02 23:31 | +10 stop | ZEC | DOWN | 0.62 | 0.44 | -2.15 |
| 11-02 23:31 | +20 | ZEC | DOWN | 0.62 | open |  |
| 11-02 23:31 | +15 | ZEC | DOWN | 0.63 | open |  |
| 11-02 23:31 | +10 | ZEC | DOWN | 0.63 | open |  |
| 11-02 23:31 | +5 | ZEC | DOWN | 0.63 | open |  |
| 11-02 23:31 | +10 stop | NEAR | DOWN | 0.62 | 0.44 | -2.15 |
| 11-02 23:31 | +20 | NEAR | DOWN | 0.62 | yes | -6.37 |
| 11-02 23:31 | +15 | NEAR | DOWN | 0.62 | yes | -6.37 |
| 11-02 23:31 | +10 | NEAR | DOWN | 0.62 | yes | -6.37 |
| 11-02 23:31 | +5 | NEAR | DOWN | 0.62 | yes | -6.37 |
| 11-02 23:31 | +10 stop | DOGE | DOWN | 0.63 | 0.37 | -2.94 |
| 11-02 23:31 | +20 | DOGE | DOWN | 0.63 | open |  |
| 11-02 23:31 | +15 | DOGE | DOWN | 0.63 | open |  |
| 11-02 23:31 | +10 | DOGE | DOWN | 0.63 | open |  |
| 11-02 23:31 | +5 | DOGE | DOWN | 0.63 | open |  |
| 11-02 23:30 | +10 stop | ETH | UP | 0.58 | 0.43 | -1.86 |
| 11-02 23:30 | +20 | ETH | UP | 0.59 | 0.82 | 2.02 |
